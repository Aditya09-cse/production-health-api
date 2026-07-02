# Deployment Guide

## Local Setup

```bash
git clone https://github.com/Aditya09-cse/production-health-api.git
cd production-health-api

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

## Docker

```bash
docker compose build
docker compose up -d
```

## AWS

- Launch Ubuntu EC2
- Install Docker
- Install Docker Compose
- Clone Repository
- Configure IAM Role
- Configure Security Group
- Start Container

```bash
docker compose up -d
```

## CI/CD

Every push to `main` automatically:

- Builds Docker Image
- Pushes Docker Image
- Deploys to EC2