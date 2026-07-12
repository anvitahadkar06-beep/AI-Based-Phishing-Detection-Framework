"""
=========================================================
AI Based Phishing Detection Framework

Model Evaluation Script
=========================================================
"""

import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

# =====================================================
# Paths
# =====================================================

DATASET_PATH = "data/processed/features_dataset.csv"

MODEL_PATH = "models/phishing_detector.pkl"

FIGURE_DIR = "reports/figures"

REPORT_DIR = "reports/evaluation"

os.makedirs(FIGURE_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

X = df.drop("label", axis=1)
y = df["label"]

# Same split as training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =====================================================
# Load Model
# =====================================================

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

print("Model Loaded Successfully")

# =====================================================
# Prediction
# =====================================================

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = f1_score(y_test, pred)

print("\nAccuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))

# =====================================================
# Save Classification Report
# =====================================================

report = classification_report(y_test, pred)

with open(os.path.join(REPORT_DIR, "model_report.txt"), "w") as f:
    f.write("AI Based Phishing Detection Framework\n\n")
    f.write(f"Accuracy : {accuracy:.4f}\n")
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall   : {recall:.4f}\n")
    f.write(f"F1 Score : {f1:.4f}\n\n")
    f.write(report)

print("Model report saved.")

# =====================================================
# Confusion Matrix
# =====================================================

cm = confusion_matrix(y_test, pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

plt.figure(figsize=(6, 6))
disp.plot()
plt.title("Confusion Matrix")
plt.savefig(os.path.join(FIGURE_DIR, "confusion_matrix.png"))
plt.close()

print("Confusion Matrix saved.")

# =====================================================
# ROC Curve
# =====================================================

plt.figure(figsize=(6, 6))

RocCurveDisplay.from_estimator(model, X_test, y_test)

plt.title("ROC Curve")

plt.savefig(os.path.join(FIGURE_DIR, "roc_curve.png"))

plt.close()

print("ROC Curve saved.")

# =====================================================
# Feature Importance
# =====================================================

importance = model.feature_importances_

feature_importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": importance

})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(figsize=(12, 8))

plt.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.gca().invert_yaxis()

plt.title("Feature Importance")

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "feature_importance.png"
    )
)

plt.close()

print("Feature Importance saved.")

# =====================================================

print("\n")
print("=" * 60)
print("Evaluation Completed Successfully")
print("=" * 60)

print("\nGenerated Files:")

print("reports/figures/confusion_matrix.png")

print("reports/figures/roc_curve.png")

print("reports/figures/feature_importance.png")

print("reports/evaluation/model_report.txt")