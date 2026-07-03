"""
decision_engine.py

Final Hybrid Decision Engine for Phishing Detection:
- Machine Learning Model (Random Forest)
- Rule-Based System
- Trusted Domain Override (HIGHEST PRIORITY)
"""

from model_loader import load_model
from rule_engine import analyze_rules
from trusted_domains import is_trusted
import pandas as pd

# Load model once (important for performance)
model, feature_columns = load_model()


def decide(url, features):
    """
    Final decision engine

    Parameters:
        url (str): input URL
        features (dict): extracted URL features

    Returns:
        dict: final prediction result
    """

    # -----------------------------
    # Validate input
    # -----------------------------
    if not isinstance(features, dict):
        raise ValueError("Features must be a dictionary")

    # -----------------------------
    # Convert features → DataFrame
    # -----------------------------
    input_df = pd.DataFrame([features])

    # Fill missing columns safely
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Ensure correct column order
    input_df = input_df[feature_columns]

    # -----------------------------
    # ML MODEL PREDICTION
    # -----------------------------
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    confidence = float(max(probabilities) * 100)

    result_label = "PHISHING" if prediction == 1 else "LEGITIMATE"

    # -----------------------------
    # RULE ENGINE
    # -----------------------------
    rule_result = analyze_rules(features)
    rule_score = rule_result.get("rule_score", 0)
    reasons = rule_result.get("reasons", [])

    # -----------------------------
    # TRUSTED DOMAIN CHECK (HIGHEST PRIORITY)
    # -----------------------------
    trusted = is_trusted(url)

    if trusted:
        result_label = "LEGITIMATE"
        risk = "LOW"
        confidence = 99.0  # override for clean UX

        return {
            "url": url,
            "prediction": result_label,
            "confidence": confidence,
            "risk": risk,
            "trusted": trusted,
            "rule_score": rule_score,
            "reasons": ["Trusted domain - safe override"]
        }

    # -----------------------------
    # FINAL RISK LOGIC (NON-TRUSTED CASES)
    # -----------------------------
    if result_label == "LEGITIMATE":

        if rule_score <= 20:
            risk = "LOW"
        elif rule_score <= 40:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

    else:
        # PHISHING CASE
        if confidence >= 90 or rule_score >= 60:
            risk = "HIGH"
        elif confidence >= 70 or rule_score >= 35:
            risk = "MEDIUM"
        else:
            risk = "LOW"

    # -----------------------------
    # FINAL OUTPUT
    # -----------------------------
    return {
        "url": url,
        "prediction": result_label,
        "confidence": round(confidence, 2),
        "risk": risk,
        "trusted": trusted,
        "rule_score": rule_score,
        "reasons": reasons
    }