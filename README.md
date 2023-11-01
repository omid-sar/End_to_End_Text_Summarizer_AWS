# End to End Text Summarizer Project

## Overview
This project is an end-to-end text summarization solution, designed to condense lengthy texts while retaining the essential information. It involves various components and requires a series of updates to configuration files and source code to ensure seamless operation.

## Getting Started

### Prerequisites
- Conda (Miniconda or Anaconda)
- Python 3.8

### Installation Steps
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/omid-sar/End_to_End_Text_Summarizer_AWS
   cd End_to_End_Text_Summarizer_AWS
   ```

2. **Create and Activate a Conda Environment**: 
   ```bash
   conda create -n summary python=3.8 -y
   conda activate summary
   ```

3. **Install the Requirements**: 
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**: 
   ```bash
   python app.py
   ```

   After running, access the application via your local host and specified port.

## Workflows and Updates
Ensure to sequentially update the following components for optimal performance:

1. `config.yaml`
2. `params.yaml`
3. Entity configurations
4. Configuration manager in `src/config`
5. Components
6. Pipeline
7. `main.py`
8. `app.py`

## Contact
- **Author**: Omid Sar
- **Email**: [mr.omid.sardari@gmail.com](mailto:mr.omid.sardari@gmail.com)

---

# AWS CI/CD Deployment with Github Actions

## Overview
This guide provides a comprehensive walkthrough for deploying a Dockerized application on AWS EC2 using Github Actions for continuous integration and continuous deployment (CI/CD).

## Prerequisites
- AWS Account
- Github Account

## Steps

### 1. AWS Console Preparation
   - **Login**: Ensure you are logged into your AWS console.
   - **Create IAM User**: Ensure the user has the following policies:
     - `AmazonEC2ContainerRegistryFullAccess`
     - `AmazonEC2FullAccess`
   - **Create ECR Repository**: Note down the URI.

### 2. EC2 Instance Setup
   - **Create an EC2 Instance**: Preferably Ubuntu.
   - **Install Docker on EC2**: 
     - Optional: Update and upgrade the system.
       ```bash
       sudo apt-get update -y
       sudo apt-get upgrade
       ```
     - Required: Install Docker.
       ```bash
       curl -fsSL https://get.docker.com -o get-docker.sh
       sudo sh get-docker.sh
       sudo usermod -aG docker ubuntu
       newgrp docker
       ```

### 3. Configure Self-hosted Runner on Github
   - Navigate to your repository's settings.
   - Go to Actions > Runners.
   - Click "New self-hosted runner" and follow the instructions.

### 4. Set Up Github Secrets
   - Navigate to your repository's settings.
   - Go to Secrets and add the following:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `AWS_REGION`
     - `AWS_ECR_LOGIN_URI`
     - `ECR_REPOSITORY_NAME`

## Deployment Flow
1. **Build Docker Image**: Locally or in CI/CD pipeline.
2. **Push Docker Image to ECR**: Use AWS CLI or Github Actions.
3. **Launch EC2 Instance**: Ensure it has Docker installed.
4. **Pull Docker Image on EC2**: Use AWS CLI.
5. **Run Docker Container on EC2**: Start your application.
```

