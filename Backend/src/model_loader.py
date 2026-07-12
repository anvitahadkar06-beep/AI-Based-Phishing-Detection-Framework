import os
import joblib

# Backend folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_detector.pkl")
FEATURE_PATH = os.path.join(BASE_DIR, "models", "feature_columns.pkl")


def load_model():
    """
    Loads the trained model and expected feature columns.
    """

    model = joblib.load(MODEL_PATH)
    feature_columns = joblib.load(FEATURE_PATH)

    return model, feature_columns