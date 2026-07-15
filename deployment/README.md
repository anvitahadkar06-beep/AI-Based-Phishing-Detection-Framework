# 🚀 Deployment Guide

This directory contains the deployment documentation, configuration guidelines, and operational instructions for the **AI-Based Phishing Detection Framework**.

The project follows a **decoupled client-server architecture**, where the frontend and backend are deployed independently to improve scalability, maintainability, and ease of future development.

---

# 🌐 Deployment Overview

The application consists of two independently deployed components:

| Component | Technology | Deployment Platform |
|------------|------------|---------------------|
| Frontend | React + Vite | Vercel |
| Backend | Flask REST API | Render |

The React frontend communicates with the Flask backend using REST API calls over HTTP.

---

# 🏗️ Deployment Architecture

```text
                    User
                      │
                      ▼
        React Frontend (Vercel)
                      │
              HTTP Requests
                      │
                      ▼
         Flask REST API (Render)
                      │
          Feature Extraction Module
                      │
                      ▼
          Hybrid Decision Engine
          ┌───────────┴───────────┐
          ▼                       ▼
  Machine Learning Model     Rule Engine
          │                       │
          └───────────┬───────────┘
                      ▼
            Prediction Response
                      │
                      ▼
               React Frontend
```

---

# 📂 Deployment Files

The deployment process relies on the following configuration files located in the project root.

| File | Description |
|------|-------------|
| `requirements.txt` | Python dependencies required by the Flask backend |
| `Procfile` | Startup command used by Render |
| `.env.example` | Template for environment variables |
| `README.md` | Main project documentation |

---

# 🔌 API Configuration

The frontend communicates with the backend using REST API endpoints.

## Development Environment

Frontend

```
http://localhost:5173
```

↓

Backend

```
http://127.0.0.1:5000
```

The frontend sends HTTP requests to:

| Method | Endpoint | Purpose |
|---------|----------|----------|
| GET | `/` | Check backend availability |
| GET | `/health` | Health monitoring |
| POST | `/predict` | Analyze URLs and return phishing prediction |

---

## Production Environment

After deployment, update the frontend API URL to point to the deployed Render backend.

Example:

```
https://your-render-service.onrender.com/predict
```

---

# 💻 Local Operational Commands

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Based-Phishing-Detection-Framework.git
cd AI-Based-Phishing-Detection-Framework
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start the Flask Backend

```bash
cd src
python app.py
```

The backend will start at

```
http://127.0.0.1:5000
```

---

## 5. Start the React Frontend

Open a **new terminal**.

Navigate to the frontend directory.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Start the development server.

```bash
npm run dev
```

The frontend will be available at

```
http://localhost:5173
```

---

# ⚙️ Backend Deployment (Render)

The backend is deployed as a **Python Web Service** using Render.

Render was selected because it provides:

- Native Python support
- Automatic GitHub deployments
- Free HTTPS
- Environment variable management
- Procfile support
- Continuous deployment after Git pushes

---

## Backend Deployment Steps

### Step 1

Push the latest backend code to GitHub.

```bash
git add .
git commit -m "Backend updates"
git push origin <branch-name>
```

---

### Step 2

Create a new **Python Web Service** on Render.

Connect the GitHub repository.

---

### Step 3

Configure the deployment.

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
python src/app.py
```

---

### Step 4

Configure any required environment variables using the Render dashboard.

---

### Step 5

Deploy the application.

After deployment, verify:

```
https://your-render-service.onrender.com/
```

Expected Response

```json
{
  "message":"AI-Based Phishing Detection Backend",
  "status":"Running"
}
```

---

# 💻 Frontend Deployment (Vercel)

The frontend is deployed using **Vercel**.

Vercel was selected because it provides:

- Native React support
- Automatic GitHub deployments
- Fast global CDN
- HTTPS by default
- Zero-configuration deployment

---

## Frontend Deployment Steps

### Step 1

Push the latest frontend code to GitHub.

```bash
git add .
git commit -m "Frontend updates"
git push origin <branch-name>
```

---

### Step 2

Import the repository into Vercel.

Select the repository.

---

### Step 3

Configure build settings.

Framework

```
Vite
```

Build Command

```bash
npm run build
```

Output Directory

```
dist
```

---

### Step 4

Deploy the application.

After deployment, Vercel generates a public application URL.

---

# 🔄 Deployment Workflow

```text
Developer
     │
     ▼
Push Changes to GitHub
     │
     ├──────────────┐
     ▼              ▼
Render         Vercel
(Backend)     (Frontend)
     │              │
     └──────┬───────┘
            ▼
     Live Application
```

---

# 🧪 Deployment Verification

After deployment, verify the following.

## Backend

### Home Endpoint

```
GET /
```

Expected Response

```json
{
  "message":"AI-Based Phishing Detection Backend",
  "status":"Running"
}
```

---

### Health Endpoint

```
GET /health
```

Expected Response

```json
{
  "status":"healthy"
}
```

---

### Prediction Endpoint

```
POST /predict
```

Example Request

```json
{
  "url":"https://google.com"
}
```

Expected Response

```json
{
  "prediction":"LEGITIMATE",
  "confidence":99.0,
  "risk":"LOW",
  "trusted":true,
  "rule_score":0,
  "reasons":[
    "Trusted domain - safe override"
  ]
}
```

---

## Frontend

Open the deployed Vercel application.

Verify that:

- The application loads successfully.
- URLs can be analyzed.
- Prediction results are displayed.
- Confidence scores are shown.
- Risk levels are displayed.
- Detection reasons are returned.
- Backend communication succeeds without errors.

---

# 🐳 Docker Deployment

Docker support is **not currently included** in this project.

To support containerized deployment in the future, the following files would be required:

- `Dockerfile`
- `docker-compose.yml`
- Container networking configuration
- Environment variable configuration

The current implementation uses Render and Vercel for deployment instead of Docker containers.

---

# 🛠️ Troubleshooting

## Backend does not start

- Verify that all dependencies are installed.
- Check `requirements.txt`.
- Verify the startup command in the `Procfile`.

---

## Frontend cannot connect to the backend

- Verify the backend deployment URL.
- Ensure the frontend API endpoint points to the deployed backend.
- Confirm Flask CORS is enabled.

---

## Build fails

- Verify Python and Node.js versions.
- Ensure all dependencies are installed.
- Review deployment logs for missing packages or configuration errors.

---

# 📖 Additional Information

For project setup, source code documentation, datasets, API specifications, and local development instructions, refer to the main project **README.md** located in the repository root.
