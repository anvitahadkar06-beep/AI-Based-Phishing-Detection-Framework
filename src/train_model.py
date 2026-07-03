"""
=========================================================
AI Based Phishing Detection Framework

Final Model Training Script
=========================================================
"""

import os
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# =====================================================
# Paths
# =====================================================

DATASET_PATH = "data/processed/features_dataset.csv"

MODEL_DIR = "models"

MODEL_PATH = os.path.join(MODEL_DIR, "phishing_detector.pkl")

FEATURE_PATH = os.path.join(MODEL_DIR, "feature_columns.pkl")

# =====================================================
# Create models folder
# =====================================================

os.makedirs(MODEL_DIR, exist_ok=True)

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

print(df.head())

print("\nDataset Shape :", df.shape)

# =====================================================
# Features
# =====================================================

X = df.drop("label", axis=1)

y = df["label"]

feature_columns = list(X.columns)

print("\nNumber of Features :", len(feature_columns))

# =====================================================
# Train Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("\nTraining Samples :", len(X_train))

print("Testing Samples :", len(X_test))

# =====================================================
# Model
# =====================================================

print("\nTraining Random Forest...")

model = RandomForestClassifier(

    n_estimators=300,

    max_depth=15,

    random_state=42,

    class_weight="balanced"

)

model.fit(X_train, y_train)

print("Training Completed")

# =====================================================
# Prediction
# =====================================================

pred = model.predict(X_test)

# =====================================================
# Metrics
# =====================================================

accuracy = accuracy_score(y_test, pred)

precision = precision_score(y_test, pred)

recall = recall_score(y_test, pred)

f1 = f1_score(y_test, pred)

print("\n")

print("=" * 60)

print("MODEL PERFORMANCE")

print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")

print(f"Precision: {precision:.4f}")

print(f"Recall   : {recall:.4f}")

print(f"F1 Score : {f1:.4f}")

print("\nClassification Report\n")

print(classification_report(y_test, pred))

print("Confusion Matrix\n")

print(confusion_matrix(y_test, pred))

# =====================================================
# Save Model
# =====================================================

with open(MODEL_PATH, "wb") as file:

    pickle.dump(model, file)

with open(FEATURE_PATH, "wb") as file:

    pickle.dump(feature_columns, file)

print("\n")

print("=" * 60)

print("FILES SAVED")

print("=" * 60)

print("Model Saved At")

print(MODEL_PATH)

print()

print("Feature Columns Saved At")

print(FEATURE_PATH)

print()

print("Training Completed Successfully")