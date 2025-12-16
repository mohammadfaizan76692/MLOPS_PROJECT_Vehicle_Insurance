# 🚗 Vehicle Data End-to-End MLOps Project

> **A complete production-grade Machine Learning system — from raw data ingestion to cloud deployment with CI/CD.**

This project demonstrates how to build a **scalable, modular, and industry-ready MLOps pipeline** using **Python, MongoDB, AWS, Docker, and GitHub Actions**.
It closely mirrors **real-world ML engineering workflows** followed in production environments.

---

## 🚀 What This Project Demonstrates

* ✅ End-to-end **ML pipeline architecture**
* ✅ Clean & modular **project template**
* ✅ **MongoDB Atlas** for real-world data ingestion
* ✅ **Schema-based data validation**
* ✅ Feature engineering & transformation pipelines
* ✅ **Model training, evaluation & versioning**
* ✅ **AWS S3-based model registry**
* ✅ **Dockerized ML application**
* ✅ **CI/CD pipeline using GitHub Actions**
* ✅ **Self-hosted GitHub Runner on EC2**
* ✅ **Production inference API with Flask**

---

## 🧱 Project Architecture

```
Raw Data (MongoDB)
        ↓
Data Ingestion
        ↓
Data Validation
        ↓
Data Transformation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Pusher (AWS S3)
        ↓
Prediction Pipeline (Flask API)
        ↓
Docker + CI/CD + EC2 Deployment
```

---

## 📁 Project Structure

```bash
├── src/
│   ├── components/            # ML pipeline components
│   ├── configuration/         # MongoDB & AWS configurations
│   ├── constants/             # Global constants & configs
│   ├── data_access/           # MongoDB data access logic
│   ├── entity/                # Config & artifact entities
│   ├── logger/                # Centralized logging
│   ├── exception/             # Custom exception handling
│   ├── aws_storage/           # S3 model push/pull logic
│   └── utils/                 # Utility functions
├── notebook/                  # EDA & MongoDB demo notebooks
├── templates/                 # HTML templates
├── static/                    # CSS / static files
├── app.py                     # Prediction API
├── demo.py                    # Pipeline testing script
├── requirements.txt
├── setup.py
├── pyproject.toml
├── Dockerfile
├── .dockerignore
└── .github/workflows/aws.yaml
```

---

## ⚙️ Local Project Setup

### 1️⃣ Create Project Template

```bash
python template.py
```

---

### 2️⃣ Configure Local Packages

* Implement local package imports using:

  * `setup.py`
  * `pyproject.toml`
* 📘 Reference file: `crashcourse.txt`

---

### 3️⃣ Create Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

---

### 4️⃣ Verify Installation

```bash
pip list
```

✔ Confirms local project packages are installed correctly.

---

## 🍃 MongoDB Atlas Setup

1. Create an account on **MongoDB Atlas**
2. Create a new project → Create Cluster (M0 – Free Tier)
3. Create a **Database User**
4. Add Network Access:

   ```
   0.0.0.0/0
   ```
5. Get Python connection string
6. Replace password and store securely

---

### MongoDB Data Flow

* Dataset placed inside `notebook/`
* Data pushed using `mongoDB_demo.ipynb`
* Verified via:

  ```
  MongoDB Atlas → Database → Browse Collections
  ```

---

## 🧠 Logging, Exception Handling & EDA

* Centralized logging module
* Custom exception handling
* Tested via `demo.py`
* EDA & Feature Engineering notebooks included

---

## 🔄 Data Ingestion Pipeline

* MongoDB → Python → Pandas DataFrame
* Config-driven ingestion
* Artifact tracking enabled

### Environment Variable Setup

**Bash**

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@..."
```

**PowerShell**

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>@..."
```

📌 `artifact/` directory is ignored via `.gitignore`

---

## ✅ Data Validation & Transformation

* Schema validation using `schema.yaml`
* Data drift & missing value checks
* Feature engineering pipeline
* Reusable transformers

---

## 🤖 Model Training

* Custom estimator classes
* Config-driven training
* Model artifacts stored
* Threshold-based model comparison

---

## 📊 Model Evaluation & Registry (AWS S3)

* AWS IAM user setup
* S3 bucket for model registry
* Automatic comparison with previous models
* Only better models get pushed

### Required Constants

```python
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"
```

---

## 🌐 Prediction Pipeline

* Flask-based inference API
* `/predict` → Real-time predictions
* `/training` → Trigger model training

---

## 🐳 Docker & CI/CD Pipeline

* Dockerized application
* GitHub Actions workflow
* Self-hosted GitHub Runner on EC2
* AWS ECR for Docker image storage

---

## ☁️ Deployment on AWS EC2

* Ubuntu 24.04 EC2 instance
* Docker installed on server
* Port **5000** enabled

### Access the Application

```
http://<EC2_PUBLIC_IP>:5000
```

---

## 🔐 GitHub Secrets Used

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_DEFAULT_REGION`
* `ECR_REPO`

---

## 🏁 Final Outcome

✔ Fully automated ML lifecycle
✔ Production-ready deployment
✔ Real-world MLOps practices
✔ Scalable & maintainable codebase

---

## 🙌 Author

**Mohd Faizan**
Data Scientist | Machine Learning Engineer
Focused on **Deep Learning, MLOps & Production ML Systems**

---

⭐ **If you like this project, don’t forget to star the repo!**
