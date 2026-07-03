import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_detector.pkl")
FEATURE_COLUMNS_PATH = os.path.join(BASE_DIR, "models", "feature_columns.pkl")

HOST = "0.0.0.0"
PORT = 5000
DEBUG = True

APP_NAME = "AI Based Phishing Detection Framework"
VERSION = "1.0.0"