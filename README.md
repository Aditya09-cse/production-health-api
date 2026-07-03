# 🚀 Production Health API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-success)
![CloudWatch](https://img.shields.io/badge/Monitoring-CloudWatch-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

Production Health API is a production-style Flask REST API demonstrating end-to-end DevOps practices.

The project includes:

- Dockerized Flask API
- GitHub Actions CI/CD
- AWS EC2 Deployment
- Amazon S3 Backup
- CloudWatch Monitoring
- IAM Least Privilege
- Docker Compose
- Gunicorn
- k6 Performance Testing

---

# 🚀 Features

- REST API
- CRUD Notes API
- Health Endpoint
- Metrics Endpoint
- Amazon S3 Backup
- Docker
- Docker Compose
- AWS EC2
- GitHub Actions CI/CD
- CloudWatch Dashboard
- CloudWatch Alarm
- IAM Role
- Logging
- k6 Load Testing

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Flask |
| Container | Docker |
| Cloud | AWS EC2 |
| Storage | Amazon S3 |
| CI/CD | GitHub Actions |
| Monitoring | CloudWatch |
| Load Testing | k6 |
| Testing | Postman |
| Production Server | Gunicorn |

---

# 🏗 Architecture

```
Developer
      │
Git Push
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
Docker Build
      │
Docker Hub
      │
      ▼
AWS EC2
      │
Docker Compose
      │
Gunicorn
      ▼
Flask API
      │
 ├────────► Amazon S3
 │
 └────────► CloudWatch
```

---

# 📁 Project Structure

```text
production-health-api/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.py
│
├── routes/
├── utils/
├── tests/
├── docs/
├── data/
└── logs/
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /health | Health Check |
| GET | /metrics | System Metrics |
| GET | /notes | Get Notes |
| POST | /notes | Create Note |
| PUT | /notes/<id> | Update Note |
| DELETE | /notes/<id> | Delete Note |
| POST | /backup | Upload Backup to Amazon S3 |

---

# 🐳 Docker

```bash
docker compose build
docker compose up -d
```

---

# ☁ AWS Deployment

- Ubuntu EC2
- Docker
- Docker Compose
- IAM Role
- Amazon S3
- Security Groups

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically:

- Checkout Repository
- Build Docker Image
- Push Docker Image
- Deploy to AWS EC2

---

# 📈 Monitoring

Amazon CloudWatch provides

- CPU Utilization
- Network In
- Network Out
- Status Checks
- CPU Alarm

---

# ⚡ Load Testing

Tool Used

- k6

Results

- 20 Virtual Users
- 60 Seconds
- 396 Requests
- 100% Success Rate
- 0% Errors
- Average Response Time: 1.79s

---

# 🔐 Security

- IAM Least Privilege
- EC2 Security Groups
- Environment Variables
- Docker Isolation
- CloudWatch Monitoring

---

# 📷 Screenshots

```
docs/screenshots/
```

Contains

- Docker
- EC2
- GitHub Actions
- CloudWatch
- k6
- S3
- Postman

---

# 🚀 Future Improvements

- Kubernetes Deployment
- Terraform
- HTTPS with Nginx
- Prometheus
- Grafana
- Auto Scaling
- Load Balancer

---

# 👨‍💻 Author

**Aditya Singh Tomar**

DevOps | Cloud | AWS | Docker | CI/CD

GitHub

https://github.com/Aditya09-cse

LinkedIn


https://www.linkedin.com/in/aditya-tomar-42731628a
