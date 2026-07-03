import pandas as pd

def run_pipeline():

    # Load datasets
    phishing = pd.read_csv("data/raw/phishing.csv")
    legitimate = pd.read_csv("data/raw/legitimate.csv")

    print("Phishing shape:", phishing.shape)
    print("Legitimate shape:", legitimate.shape)

    # IMPORTANT: your dataset already has features
    # So we DO NOT try to extract URL column

    # Ensure label exists
    if "label" not in phishing.columns:
        phishing["label"] = 1

    if "label" not in legitimate.columns:
        legitimate["label"] = 0

    # Combine
    df = pd.concat([phishing, legitimate], ignore_index=True)

    # Clean
    df = df.dropna()
    df = df.drop_duplicates()

    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save
    output_path = "data/processed/master_dataset.csv"
    df.to_csv(output_path, index=False)

    print("\n✅ DATA COLLECTION SUCCESSFUL")
    print("Final dataset shape:", df.shape)
    print("Saved at:", output_path)


if __name__ == "__main__":
    run_pipeline()