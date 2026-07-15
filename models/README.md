# 🤖 Machine Learning Models

This directory contains the trained machine learning model and supporting metadata required for phishing URL detection. These files are generated during the model training process and loaded by the backend during inference.

The models are serialized using **Pickle (.pkl)** to enable efficient loading and real-time predictions without retraining.

---

# 📂 Directory Structure

```
models/
├── phishing_detector.pkl      # Trained Random Forest classification model
├── feature_columns.pkl        # Ordered feature metadata used during inference
└── README.md                  # Documentation for trained models
```

---

# 📦 Model Files

## `phishing_detector.pkl`

This file contains the trained **Random Forest Classifier** responsible for predicting whether a submitted URL is **Legitimate** or **Phishing**.

### Model Responsibilities

- Classifies URLs using extracted features.
- Generates prediction probabilities.
- Returns confidence scores used by the decision engine.
- Integrates with the hybrid detection pipeline.

The model is loaded dynamically by the backend through:

```python
src/model_loader.py
```

---

## `feature_columns.pkl`

Machine learning models require input features to be presented in the exact order used during training.

This file stores the expected feature names and ordering, ensuring consistency between training and inference.

### Responsibilities

- Maintains feature ordering.
- Prevents feature mismatch errors.
- Ensures reliable predictions.
- Supports future model retraining.

---

# ⚙️ Model Loading Workflow

The backend automatically loads both files during application startup.

```
Application Start
        │
        ▼
Load feature_columns.pkl
        │
        ▼
Load phishing_detector.pkl
        │
        ▼
Ready for Predictions
```

The loading process is handled by:

```text
src/model_loader.py
```

---

# 🔄 Prediction Pipeline

The trained model is used as part of the hybrid phishing detection framework.

```
User URL
    │
    ▼
Feature Extraction
    │
    ▼
Feature Vector
    │
    ▼
Random Forest Model
    │
    ▼
Prediction Probability
    │
    ▼
Hybrid Decision Engine
    │
    ▼
Final Classification
```

The machine learning prediction is combined with:

- Rule-based phishing analysis
- Trusted domain verification

to produce the final detection result.

---

# 📊 Model Information

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Classifier |
| Framework | Scikit-learn |
| Model Format | Pickle (`.pkl`) |
| Input | Engineered URL Features |
| Output | Legitimate / Phishing |
| Confidence | Prediction Probability |

---

# 📌 Notes

- These files should **not be modified manually**.
- Any changes to the feature extraction process require the model to be retrained.
- If the model is retrained, both `phishing_detector.pkl` and `feature_columns.pkl` should be regenerated together to maintain compatibility.
- The backend expects these files to remain inside the `models/` directory for successful loading during inference.
