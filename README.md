# End-to-End CI/CD Automation & Cloud Deployment for Gohel Tailors Web Application

## 📌 Overview
This repository contains the complete source code, configuration files, and DevOps workflows used to build, containerize, deploy, and monitor the **Gohel Tailors Web Application**.  
The project implements a **full CI/CD pipeline** using GitHub → Jenkins → Docker → Docker Hub → AWS ECS Fargate, with metrics and dashboards powered by **Prometheus & Grafana**.

The goal of this project is to eliminate manual deployments, achieve reliable and repeatable automated updates, and ensure cloud scalability with real-time monitoring.

---

# 📁 Project Structure

```
|-- app/
| |-- app.py
| |-- requirements.txt
| |-- templates/
| |-- static/
|
|-- Dockerfile
|-- Jenkinsfile
|-- terraform/ (optional)
|-- prometheus/
| |-- prometheus.yml
|
|-- grafana/
|-- README.md
```

---

# 🚀 Features

- Fully automated CI/CD pipeline using Jenkins
- Docker containerization for consistent environment
- Docker Hub registry for hosting container images
- AWS ECS Fargate deployment (serverless containers)
- CloudWatch Logs for application-level logging
- Prometheus metrics exposure via \`/metrics\` endpoint
- Grafana dashboard for real-time visual monitoring
- MongoDB Atlas as cloud database
- Secure and scalable architecture

---

# 🏗 Architecture Flow

```
GitHub (Source Code Repository)
        │
        ▼
Jenkins (CI/CD Server on EC2)
        │
        ├── Pulls code via GitHub Webhook
        ├── Builds Docker Image
        ├── Logs into Docker Hub
        ├── Pushes Image to Docker Hub
        ├── Deploys on ECS using AWS CLI
        ▼
Docker Hub (Image Registry)
        │
        ▼
Amazon ECS (Fargate)
        │
        ├── Pulls latest Docker image
        ├── Runs Flask container as service
        │
        ▼
Flask Application (ECS Task)
        ├── Connects to MongoDB Atlas
        ├── Exposes /metrics for monitoring
        ▼
CloudWatch Logs

Local Monitoring System:
        ├── Prometheus (Scrapes ECS publicIP:5000/metrics)
        └── Grafana (Visualizes metrics: requests, latency, errors)
```

---

# 🖥 Tech Stack

### Backend:
- Python (Flask)

### Database:
- MongoDB Atlas

### Containerization:
- Docker
- Docker Hub

### CI/CD:
- Jenkins (Pipeline-as-Code using Jenkinsfile)
- GitHub Webhook triggers

### Cloud Platform:
- AWS ECS Fargate
- CloudWatch (Logs)
- IAM Roles, VPC, Subnets

### Monitoring:
- Prometheus (Local Docker)
- Grafana (Local Docker)

---

# 🔧 Installation & Setup

## 1. Clone the Repository
```bash
git clone https://github.com/prashantgohel321/Gohel-Tailors.git
cd <repo-name>
```

---

# 🐳 Docker Setup

## Build Image
```bash
docker build -t gohel-tailors-app .
```

## Run Container Locally
```bash
docker run -p 5000:5000 gohel-tailors-app
```

---

# 🔁 Jenkins CI/CD Pipeline (Using Jenkinsfile)

### Pipeline Stages:
1. Pull code from GitHub
2. Install dependencies
3. Build Docker image
4. Login to Docker Hub
5. Push image to repository
6. Deploy to AWS ECS using AWS CLI

Jenkins executes this automatically on every GitHub push.

---

# ☁ AWS Deployment (ECS Fargate)

### Requirements:
- ECS Cluster
- Task Definition (linked with Docker Hub image)
- Service running on Fargate
- Security group allowing port 5000 inbound
- IAM role for ECS tasks

### Jenkins Deployment Command:
```bash
aws ecs update-service --cluster <cluster-name> --service <service-name> --force-new-deployment
```
This pulls the **latest Docker image** and redeploys the app.

---

# 📊 Monitoring (Prometheus + Grafana)

### Step 1: Run Prometheus Locally
Inside prometheus.yml:
```yaml
scrape_configs:

job_name: 'ecs-app'
static_configs:

targets: ['<ecs-public-ip>:5000']
```

### Step 2: Run Prometheus
```bash
docker run -p 9090:9090 -v ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

### Step 3: Run Grafana
```bash
docker run -p 3000:3000 grafana/grafana
```

### Dashboards you can create:
- Request Rate
- Latency
- Error Rate
- Uptime
- Custom Flask counters

---

# 📂 Environment Variables

The app requires:
```env
MONGO_URI
SECRET_KEY
ENV=production
```

Set these in:
- Jenkins
- ECS Task Definition

---

# 🧪 Testing

### Manual Testing:
- Login
- Place Order
- Services
- Admin Dashboard
- ECS Deployment Check

### Pipeline Testing:
- Jenkins build logs
- Docker image correctness
- ECS redeployment success

### Monitoring Testing:
- Prometheus target health
- Grafana dashboards rendering

---

# 📦 Project Outcomes

- Fully automated CI/CD pipeline
- Zero manual deployment steps
- Stable & scalable cloud hosting on AWS
- Real-time monitoring of application health
- Reduced time-to-deploy from minutes to seconds
- Application behavior now measurable & observable

---

# 🛠 Future Enhancements

- Move Prometheus/Grafana to AWS (EC2 or EKS)
- Add automated unit tests to pipeline
- Add auto-scaling in ECS
- Use AWS Secret Manager for environment variables
- Use Terraform for Infrastructure-as-Code

---

# 👤 Author

**Prashant Gohel**  
GitHub: https://github.com/prashantgohel321  
LinkedIn: https://linkedin.com/in/prashantgohel1706  

---

# 📄 License
This project is created as part of the CloudCounselage DevOps Internship.  
All rights reserved. Unauthorized reproduction or distribution is prohibited.
