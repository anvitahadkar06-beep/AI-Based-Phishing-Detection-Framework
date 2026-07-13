import joblib
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "phishing_detector.pkl"
FEATURE_PATH = BASE_DIR / "models" / "feature_columns.pkl"


def load_model():
    """
    Loads the trained model and expected feature columns.
    """
    model = joblib.load(MODEL_PATH)
    feature_columns = joblib.load(FEATURE_PATH)

    return model, feature_columns