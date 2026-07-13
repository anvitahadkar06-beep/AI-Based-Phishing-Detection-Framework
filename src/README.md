# ⚙️ Source Code

This directory contains the core Python modules that power the AI-Based Phishing Detection Framework. It includes data preprocessing utilities, feature extraction modules, machine learning pipelines, the Flask API, and supporting utilities for phishing URL detection.

---

## 📂 Core Script Architecture

### 🌐 Backend API

- ```app.py```: Flask application entry point exposing REST API endpoints for URL analysis and prediction.

- ```config.py```: Central configuration file for application settings and constants.

---

### 📊 Data Pipeline

- ```data_collection.py```: Collects phishing and legitimate URL datasets from supported data sources.

- ```data_processing.py```: Cleans, validates, and preprocesses raw datasets for model training.

- ```data_storage.py```: Performs schema validation and securely stores processed datasets.

- ```dataset_builder.py```: Combines processed data and extracted features into a final machine learning dataset.

---

### 🧠 Machine Learning

- ```feature_extraction.py```: Extracts numerical and categorical URL features used for machine learning predictions.

- ```feature_extractor.py```: Alternative feature extraction implementation used for experimentation and compatibility.

- ```model_training.py```: Trains the phishing detection model using engineered features.

- ```train_model.py```: Main training script that orchestrates the complete model training workflow.

- ```model_loader.py```: Loads trained machine learning models and feature metadata for inference.

- ```prediction.py```: Executes predictions using the trained model.

- ```evaluate_model.py```: Evaluates model performance using classification metrics.

---

### 🛡️ Detection Engine

- ```decision_engine.py```: Hybrid decision engine combining machine learning predictions, rule-based analysis, and trusted domain verification.

- ```rule_engine.py```: Applies heuristic rules to identify suspicious URL characteristics.

- ```reputation_checker.py```: Performs domain reputation verification.

- ```trusted_domains.py```: Maintains and validates trusted domain whitelist entries.

---

### 📝 Utilities

- ```logger.py```: Records scan history, prediction results, and application events.

- ```utils.py```: Provides reusable helper functions used throughout the project.

---

# 🚀 Running and Testing the Project

Follow the steps below to set up, run, and test the complete application.

---

## 📋 Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.10 or later
- Node.js 18+ and npm
- Git
  
## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Based-Phishing-Detection-Framework.git
cd AI-Based-Phishing-Detection-Framework
```

---

## 2️⃣ Create a Python Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Backend Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable:

```bash
pip install flask flask-cors pandas scikit-learn numpy joblib
```

---

## 4️⃣ Run the Flask Backend

Navigate to the source directory:

```bash
cd src
```

Start the Flask server:

```bash
python app.py
```

The backend will start on:

```
http://127.0.0.1:5000
```

Verify the backend by opening:

```
http://127.0.0.1:5000
```

Expected response:

```json
{
    "message": "AI-Based Phishing Detection Backend",
    "status": "Running"
}
```

⚠️ Make sure the virtual environment is activated before running the backend.
---

## 5️⃣ Run the React Frontend

Open **a new terminal**.

Navigate to the frontend directory:

```bash
cd frontend
```

Install Node dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at:

```
http://localhost:5173
```

---

# 🧪 Testing the Backend API

Ensure the Flask backend is running.

### Test the Home Endpoint

```
GET /
```

Expected Response:

```json
{
    "message": "AI-Based Phishing Detection Backend",
    "status": "Running"
}
```

---

### Test the Health Endpoint

```
GET /health
```

Expected Response:

```json
{
    "status": "healthy"
}
```

---

### Test the Prediction Endpoint

```
POST /predict
```

Request Body:

```json
{
    "url":"https://google.com"
}
```

Expected Response:

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
The backend uses Flask-CORS to enable communication between the React frontend (`localhost:5173`) and the Flask API (`localhost:5000`).
---

# 💻 Testing Through the Frontend

1. Open the React application at:

```
http://localhost:5173
```

2. Enter a valid URL in the input field.

Example:

```
https://google.com
```

3. Click the **Analyze URL** button.

4. Wait for the request to complete.

5. The application should display:

- Prediction
- Confidence Score
- Risk Level
- Trusted Status
- Detection Reasons

---

# ✅ Running Unit Tests

Run the prediction tests:

```bash
python test_prediction.py
```

Run the decision engine tests:

```bash
python test_decision_engine.py
```

If all tests pass successfully, the output should indicate that no assertions failed.

> **Note:** Keep both the Flask backend and React frontend running in separate terminals throughout development.
---

# 📋 Development Notes

During development, keep **both servers running simultaneously**:

| Terminal | Command |
|----------|---------|
| Terminal 1 | `python app.py` |
| Terminal 2 | `npm run dev` |

The React frontend communicates with the Flask backend using Axios over:

```
http://127.0.0.1:5000
```

User URL
   │
   ▼
Feature Extraction
   │
   ▼
Random Forest Model
   │
   ▼
Rule Engine
   │
   ▼
Trusted Domain Verification
   │
   ▼
Final Prediction

⚠️Stopping either server will prevent the application from functioning correctly.

# ❗ Troubleshooting

### Flask ModuleNotFoundError

Activate the virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

---

### Model File Not Found

Ensure the following files exist inside the `models/` directory:

- `phishing_detector.pkl`
- `feature_columns.pkl`

---

### Frontend Cannot Connect to Backend

Verify:

- Flask is running on `http://127.0.0.1:5000`
- React is running on `http://localhost:5173`
- Axios base URL is correctly configured.
