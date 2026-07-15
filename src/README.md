# ⚙️ Source Code

This directory contains the core backend source code for the **AI-Based Phishing Detection Framework**. It includes the Flask REST API, data preprocessing modules, feature engineering utilities, machine learning pipeline, hybrid decision engine, and supporting helper modules used for phishing URL detection.

The source code follows a modular architecture, allowing each component to perform a dedicated task while remaining loosely coupled for easier maintenance, testing, and future scalability.

---

# 📂 Core Script Architecture

## 🌐 Backend API

### `app.py`

Flask application entry point that exposes REST API endpoints for phishing URL detection, health monitoring, and communication with the frontend.

### `config.py`

Stores application-wide configuration values, constants, and runtime settings.

---

## 📊 Data Pipeline

### `data_collection.py`

Collects phishing and legitimate URL datasets from supported data sources.

### `data_processing.py`

Performs data cleaning, preprocessing, normalization, validation, and dataset preparation for machine learning.

### `data_storage.py`

Applies schema validation rules and securely stores processed datasets.

### `dataset_builder.py`

Builds the final machine learning dataset by combining extracted features and processed data.

---

## 🧠 Machine Learning

### `feature_extraction.py`

Extracts numerical and categorical URL features used by the machine learning model.

### `feature_extractor.py`

Legacy feature extraction implementation maintained for compatibility and experimentation.

### `model_training.py`

Handles the machine learning model training pipeline.

### `train_model.py`

Main script used to train, evaluate, and save the phishing detection model.

### `model_loader.py`

Loads the trained machine learning model and feature metadata during application startup.

### `prediction.py`

Executes predictions using the trained Random Forest model.

### `evaluate_model.py`

Evaluates model performance using standard machine learning metrics.

---

## 🛡️ Detection Engine

### `decision_engine.py`

Implements the hybrid detection engine by combining:

- Machine Learning prediction
- Rule-based analysis
- Trusted domain verification

to produce the final phishing classification.

### `rule_engine.py`

Applies heuristic rules to identify suspicious URL characteristics.

### `reputation_checker.py`

Performs domain reputation verification.

### `trusted_domains.py`

Maintains and validates trusted domain whitelist entries.

---

## 📝 Utilities

### `logger.py`

Records scan history, prediction results, timestamps, and application events.

### `utils.py`

Contains reusable helper functions shared across multiple modules.

---

# 🔄 Backend Execution Flow

The backend processes every submitted URL through the following pipeline:

```text
User URL
    │
    ▼
Feature Extraction
    │
    ▼
Random Forest Model
    │
    ▼
Rule-Based Analysis
    │
    ▼
Trusted Domain Verification
    │
    ▼
Hybrid Decision Engine
    │
    ▼
JSON Response
```

---

# 🚀 Running the Project

Follow the steps below to set up and run the complete application.

---

## 📋 Prerequisites

Ensure the following software is installed:

- Python 3.10 or later
- Node.js 18+
- npm
- Git

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Based-Phishing-Detection-Framework.git

cd AI-Based-Phishing-Detection-Framework
```

---

## 2️⃣ Create a Virtual Environment

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

## 3️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

If a requirements file is unavailable:

```bash
pip install flask flask-cors pandas numpy scikit-learn joblib
```

---

## 4️⃣ Run the Flask Backend

Navigate to the source directory:

```bash
cd src
```

Start the backend server:

```bash
python app.py
```

The backend will be available at:

```
http://127.0.0.1:5000
```

Verify the server by opening:

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

> **Note:** Ensure the Python virtual environment is activated before running the backend.

---

## 5️⃣ Run the React Frontend

Open a **new terminal**.

Navigate to the frontend directory:

```bash
cd frontend
```

Install frontend dependencies:

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

# 🧪 Backend API Testing

Ensure the backend server is running.

---

## Home Endpoint

```
GET /
```

Expected Response

```json
{
  "message": "AI-Based Phishing Detection Backend",
  "status": "Running"
}
```

---

## Health Endpoint

```
GET /health
```

Expected Response

```json
{
  "status": "healthy"
}
```

---

## Prediction Endpoint

```
POST /predict
```

Request Body

```json
{
  "url": "https://google.com"
}
```

Example Response

```json
{
  "prediction": "LEGITIMATE",
  "confidence": 99.0,
  "risk": "LOW",
  "trusted": true,
  "rule_score": 0,
  "reasons": [
    "Trusted domain - safe override"
  ]
}
```

> **Note:** Flask-CORS enables communication between the React frontend (`localhost:5173`) and the Flask backend (`localhost:5000`).

---

# 💻 Frontend Testing

Open:

```
http://localhost:5173
```

1. Enter a URL.
2. Click **Analyze URL**.
3. Wait for the prediction.

The application displays:

- Prediction
- Confidence Score
- Risk Level
- Trusted Status
- Detection Reasons

---

# ✅ Running Unit Tests

Run prediction tests:

```bash
python test_prediction.py
```

Run decision engine tests:

```bash
python test_decision_engine.py
```

Successful execution indicates that all assertions have passed.

---

# 📋 Development Notes

During development, keep both servers running simultaneously.

| Terminal | Command |
|----------|---------|
| Terminal 1 | `python app.py` |
| Terminal 2 | `npm run dev` |

The React frontend communicates with the Flask backend using REST APIs over:

```
http://127.0.0.1:5000
```

Stopping either server will prevent the application from functioning correctly.

---

# ⚠️ Troubleshooting

## Flask ModuleNotFoundError

Activate the virtual environment and reinstall dependencies.

```bash
pip install -r requirements.txt
```

---

## Model Files Not Found

Ensure the following files exist inside the `models/` directory:

```
models/
├── phishing_detector.pkl
└── feature_columns.pkl
```

---

## Frontend Cannot Connect to Backend

Verify that:

- Flask is running on `http://127.0.0.1:5000`
- React is running on `http://localhost:5173`
- Flask-CORS is installed
- Axios (or Fetch API) is configured with the correct backend URL

---

# 📌 Notes

- The backend is designed using a modular architecture to improve maintainability and scalability.
- Machine learning predictions are combined with heuristic rule analysis and trusted domain verification to produce the final classification.
- Future enhancements can be implemented without modifying the frontend by extending the backend detection pipeline.
