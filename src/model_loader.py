import joblib

MODEL_PATH = "models/phishing_detector.pkl"
FEATURE_PATH = "models/feature_columns.pkl"


def load_model():
    """
    Loads the trained model and expected feature columns.
    """

    model = joblib.load(MODEL_PATH)
    feature_columns = joblib.load(FEATURE_PATH)

    return model, feature_columns