# End‑to‑End CI/CD Automation & Cloud Deployment (DevOps‑Focused Project)

<br>
<br>

- [End‑to‑End CI/CD Automation \& Cloud Deployment (DevOps‑Focused Project)](#endtoend-cicd-automation--cloud-deployment-devopsfocused-project)
  - [📌 Overview](#-overview)
  - [⚠️ Important Note About Application Code](#️-important-note-about-application-code)
  - [🎯 Project Goal](#-project-goal)
  - [📁 Repository Structure](#-repository-structure)
  - [🚀 DevOps Capabilities Demonstrated](#-devops-capabilities-demonstrated)
  - [🏗 High‑Level Architecture Flow](#-highlevel-architecture-flow)
  - [🖥 Technology Stack](#-technology-stack)
    - [CI/CD](#cicd)
    - [Containerization](#containerization)
    - [Cloud Platform](#cloud-platform)
    - [Monitoring \& Observability](#monitoring--observability)
    - [Application Layer](#application-layer)
  - [🔧 Local Setup (DevOps Validation Only)](#-local-setup-devops-validation-only)
    - [Clone Repository](#clone-repository)
    - [Build Docker Image](#build-docker-image)
    - [Run Container](#run-container)
  - [🔁 Jenkins CI/CD Pipeline](#-jenkins-cicd-pipeline)
    - [Automated Stages](#automated-stages)
  - [☁ AWS ECS Fargate Deployment](#-aws-ecs-fargate-deployment)
    - [Prerequisites](#prerequisites)
    - [Deployment Command](#deployment-command)
  - [📊 Monitoring \& Metrics](#-monitoring--metrics)
    - [Prometheus](#prometheus)
    - [Grafana](#grafana)
  - [🧪 Validation \& Testing](#-validation--testing)
    - [DevOps Validation](#devops-validation)
    - [Monitoring Validation](#monitoring-validation)
  - [📦 Key Outcomes](#-key-outcomes)
  - [🛠 Future Improvements](#-future-improvements)
  - [👤 Author](#-author)
  - [📄 License | MIT](#-license--mit)

<br>
<br>

## 📌 Overview

This repository is **intentionally DevOps‑centric**.

It contains the complete **CI/CD automation, containerization, cloud deployment, and monitoring setup** built for the *Gohel Tailors* platform. The **actual application source code is not published** in this repository due to **client/business requirements**.

The primary purpose of this project is to **showcase real‑world DevOps practices**, not the application logic itself.

The pipeline demonstrates how a production‑grade web application can be:

* Built
* Containerized
* Deployed
* Monitored
* Updated automatically

using modern DevOps tools and cloud services.

---

<br>
<br>

## ⚠️ Important Note About Application Code

* The **core web application code, UI/UX, and business logic are intentionally excluded** from this repository.
* This decision was taken to **protect client requirements and business‑specific implementation**.
* A **lightweight demo structure** is used only to validate CI/CD, containerization, and deployment flows.

👉 This repository should be evaluated **purely as a DevOps automation and cloud deployment project**.

You can check [app demo here](https://youtu.be/lkN-NC3UhJ0?si=6hVWb3jLAf89_VMp) 🙋.

And one more thing... Explanation video is coming soon...🔜

---

<br>
<br>

## 🎯 Project Goal

* Remove manual deployment steps
* Enforce repeatable and reliable releases
* Enable serverless container deployment on AWS
* Add observability using metrics and dashboards
* Represent how DevOps is applied in real client environments

---

<br>
<br>

## 📁 Repository Structure

```
|-- Dockerfile              # Container build definition
|-- Jenkinsfile             # CI/CD pipeline as code
|-- terraform/              # Infrastructure as Code (optional)
|-- prometheus/
|   |-- prometheus.yml      # Metrics scrape configuration
|-- grafana/                # Dashboards & visualization
|-- README.md
```

> Application directories such as `/app`, `/templates`, or `/static` are **not included** as part of this repository.

---

<br>
<br>

## 🚀 DevOps Capabilities Demonstrated

* End‑to‑end CI/CD pipeline using Jenkins
* Pipeline‑as‑Code via Jenkinsfile
* Docker‑based containerization for environment consistency
* Docker Hub as container image registry
* AWS ECS Fargate for serverless container deployment
* Automated redeployment on every GitHub push
* CloudWatch for application and container logs
* Prometheus metrics collection
* Grafana dashboards for real‑time monitoring
* Secure and scalable cloud architecture

---

<br>
<br>

## 🏗 High‑Level Architecture Flow

```
GitHub (Source Control)
        │
        ▼
Jenkins (CI/CD on EC2)
        │
        ├── Pulls code via GitHub webhook
        ├── Builds Docker image
        ├── Authenticates with Docker Hub
        ├── Pushes image to registry
        ├── Triggers ECS deployment via AWS CLI
        ▼
Docker Hub (Image Registry)
        │
        ▼
Amazon ECS (Fargate)
        │
        ├── Pulls latest image
        ├── Runs container as ECS Service
        │
        ▼
Application Container (ECS Task)
        ├── Emits metrics via /metrics
        ├── Sends logs to CloudWatch
        ▼
CloudWatch Logs

Monitoring (Local):
        ├── Prometheus (Metrics collection)
        └── Grafana (Visualization & dashboards)
```

---

<br>
<br>

## 🖥 Technology Stack

### CI/CD

* Jenkins
* GitHub Webhooks
* Jenkinsfile (Pipeline‑as‑Code)

### Containerization

* Docker
* Docker Hub

### Cloud Platform

* AWS ECS (Fargate)
* IAM Roles
* VPC & Subnets
* CloudWatch Logs

### Monitoring & Observability

* Prometheus
* Grafana

### Application Layer

* Flask (used only as a demo workload for DevOps validation)

---

<br>
<br>

## 🔧 Local Setup (DevOps Validation Only)

### Clone Repository

```bash
git clone https://github.com/prashantgohel321/DevOps-Project-Gohel-Tailors-Web-App.git
cd Gohel-Tailors
```

### Build Docker Image

```bash
docker build -t devops-demo-app .
```

### Run Container

```bash
docker run -p 5000:5000 devops-demo-app
```

> Note: This container exists only to validate pipeline, deployment, and monitoring.

---

<br>
<br>

## 🔁 Jenkins CI/CD Pipeline

### Automated Stages

1. Source code pull from GitHub
2. Dependency installation
3. Docker image build
4. Docker Hub authentication
5. Image push to registry
6. ECS service update using AWS CLI

Each GitHub push triggers the pipeline automatically.

---

<br>
<br>

## ☁ AWS ECS Fargate Deployment

### Prerequisites

* ECS Cluster
* Task Definition linked with Docker image
* ECS Service running on Fargate
* Security group allowing application port
* IAM role for ECS task execution

### Deployment Command

```bash
aws ecs update-service \
  --cluster <cluster-name> \
  --service <service-name> \
  --force-new-deployment
```

---

<br>
<br>

## 📊 Monitoring & Metrics

### Prometheus

* Scrapes `/metrics` endpoint from ECS task
* Validates application health and performance

```yaml
scrape_configs:
  - job_name: 'ecs-app'
    static_configs:
      - targets: ['<ecs-public-ip>:5000']
```

### Grafana

* Visualizes request rate
* Error ratio
* Latency
* Uptime
* Custom application metrics

---

<br>
<br>

## 🧪 Validation & Testing

### DevOps Validation

* Jenkins pipeline success
* Docker image integrity
* ECS redeployment verification
* Log availability in CloudWatch

### Monitoring Validation

* Prometheus target health
* Metric ingestion
* Grafana dashboard rendering

---

<br>
<br>

## 📦 Key Outcomes

* Fully automated CI/CD workflow
* Serverless container deployment on AWS
* Zero manual release steps
* Real‑time observability
* Faster, safer, repeatable deployments
* Clear separation between **DevOps infrastructure** and **application business logic**

---

<br>
<br>

## 🛠 Future Improvements

* Host Prometheus & Grafana on AWS (EC2 / EKS)
* Add automated test stages in pipeline
* Implement ECS auto‑scaling
* Use AWS Secrets Manager
* Full Infrastructure as Code via Terraform

---

<br>
<br>

## 👤 Author

**Prashant Gohel**

* GitHub: [https://github.com/prashantgohel321](https://github.com/prashantgohel321)
* LinkedIn: [https://linkedin.com/in/prashantgohel1706](https://linkedin.com/in/prashantgohel1706)

---

<br>
<br>

## 📄 License | MIT

This repository focuses on **DevOps automation and cloud deployment workflows**.

Application source code and business logic are **excluded based on client requirements**.

The DevOps implementation in this repository may be referenced for **learning and evaluation purposes only**.
