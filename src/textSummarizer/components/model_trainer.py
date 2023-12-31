import os
import torch
from textSummarizer.logging import logger
from textSummarizer.entity import ModelTrainerConfig
from transformers import AutoTokenizer, TrainingArguments, Trainer, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM
from datasets import load_from_disk

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        model_dir = os.path.join(self.config.root_dir, "pegasus-samsum-model")
        tokenizer_dir = os.path.join(self.config.root_dir, "tokenizer")

        # Check if model and tokenizer already exist
        if os.path.isdir(model_dir) and os.listdir(model_dir) and os.path.isdir(tokenizer_dir) and os.listdir(tokenizer_dir):
            logger.info("Model and tokenizer already exist. Skipping training.")
            return

        device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
        os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # Data loading
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps, per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size, weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps, evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps, save_steps=1e6, gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer = Trainer(
            model=model_pegasus, args=trainer_args, tokenizer=tokenizer, data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["test"], eval_dataset=dataset_samsum_pt["validation"]
        )

        trainer.train()

        # Save model
        model_pegasus.save_pretrained(model_dir)
        # Save tokenizer
        tokenizer.save_pretrained(tokenizer_dir)
