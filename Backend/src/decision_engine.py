"""
decision_engine.py

Hybrid Decision Engine
"""

import pandas as pd

from model_loader import load_model
from feature_extractor import extract_features
from rule_engine import analyze_rules
from trusted_domains import is_trusted

# Load model once
model, feature_columns = load_model()


def decide(url):
    """
    Hybrid decision engine.

    Parameters:
        url (str)

    Returns:
        dict
    """

    # -----------------------------
    # Extract Features
    # -----------------------------
    features_df = extract_features(url)

    features = features_df.to_dict(orient="records")[0]

    # -----------------------------
    # Create dataframe
    # -----------------------------
    input_df = pd.DataFrame([features])

    # Add missing columns
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Correct column order
    input_df = input_df[feature_columns]

    # -----------------------------
    # ML Prediction
    # -----------------------------
    prediction = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]

    confidence = float(max(probabilities) * 100)

    result_label = (
        "PHISHING"
        if prediction == 1
        else "LEGITIMATE"
    )

    # -----------------------------
    # Rule Engine
    # -----------------------------
    rule_result = analyze_rules(features)

    rule_score = rule_result.get("rule_score", 0)

    reasons = rule_result.get("reasons", [])

    # -----------------------------
    # Trusted Domain
    # -----------------------------
    trusted = is_trusted(url)

    if trusted:

        return {

            "url": url,

            "prediction": "LEGITIMATE",

            "confidence": 99.0,

            "risk": "LOW",

            "trusted": True,

            "rule_score": rule_score,

            "reasons": [
                "Trusted domain - safe override"
            ]
        }

    # -----------------------------
    # Risk Calculation
    # -----------------------------
    if result_label == "LEGITIMATE":

        if rule_score <= 20:
            risk = "LOW"

        elif rule_score <= 40:
            risk = "MEDIUM"

        else:
            risk = "HIGH"

    else:

        if confidence >= 90 or rule_score >= 60:
            risk = "HIGH"

        elif confidence >= 70 or rule_score >= 35:
            risk = "MEDIUM"

        else:
            risk = "LOW"

    return {

        "url": url,

        "prediction": result_label,

        "confidence": round(confidence, 2),

        "risk": risk,

        "trusted": trusted,

        "rule_score": rule_score,

        "reasons": reasons

    }