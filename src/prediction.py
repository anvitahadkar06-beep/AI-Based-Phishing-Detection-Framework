import pandas as pd

from feature_extractor import extract_features
from model_loader import load_model


def predict_url(url):
    """
    Predict whether a URL is phishing or legitimate.

    Returns:
        dict
    """

    model, feature_columns = load_model()

    # --------------------------
    # Feature Extraction
    # --------------------------

    features = extract_features(url)

    # Keep only expected columns
    features = features[feature_columns]

    # --------------------------
    # Prediction
    # --------------------------

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    phishing_probability = round(probabilities[1] * 100, 2)
    legitimate_probability = round(probabilities[0] * 100, 2)

    if prediction == 1:
        label = "PHISHING"
        confidence = phishing_probability
    else:
        label = "LEGITIMATE"
        confidence = legitimate_probability

    return {
        "url": url,
        "prediction": label,
        "confidence": confidence,
        "probabilities": {
            "phishing": phishing_probability,
            "legitimate": legitimate_probability
        },
        "features": features.to_dict(orient="records")[0]
    }