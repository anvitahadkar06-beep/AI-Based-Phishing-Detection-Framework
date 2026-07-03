import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model():

    df = pd.read_csv("data/processed/cleaned_dataset.csv")

    print("\n📊 Dataset Loaded:", df.shape)

    # -----------------------------
    # STEP 1: REMOVE STRING COLUMNS
    # -----------------------------
    df = df.drop(columns=["Domain"], errors="ignore")

    # Keep ONLY numeric columns
    df = df.select_dtypes(include=["number"])

    # -----------------------------
    # STEP 2: SPLIT FEATURES & LABEL
    # -----------------------------
    X = df.drop(columns=["label"])
    y = df["label"]

    # -----------------------------
    # STEP 3: TRAIN TEST SPLIT
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # -----------------------------
    # STEP 4: MODEL
    # -----------------------------
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=20,
        random_state=42
    )

    model.fit(X_train, y_train)

    # -----------------------------
    # STEP 5: PREDICTION
    # -----------------------------
    y_pred = model.predict(X_test)

    print("\n📌 Accuracy:", accuracy_score(y_test, y_pred))
    print("\n📌 Classification Report:\n")
    print(classification_report(y_test, y_pred))

    # -----------------------------
    # STEP 6: SAVE MODEL
    # -----------------------------
    joblib.dump(model, "model.pkl")

    print("\n✅ Model saved successfully")


if __name__ == "__main__":
    train_model()