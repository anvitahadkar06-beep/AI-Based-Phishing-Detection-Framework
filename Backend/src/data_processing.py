import pandas as pd
import matplotlib.pyplot as plt

plt.switch_backend('TkAgg')  # ensures plot opens in VS Code

def analyze_data():

    df = pd.read_csv("data/processed/master_dataset.csv")

    print("\n📊 DATA OVERVIEW")
    print("Shape:", df.shape)
    print(df.head())

    print("\n📌 LABEL DISTRIBUTION")
    print(df["label"].value_counts())

    print("\n📌 MISSING VALUES")
    print(df.isnull().sum())

    # -------------------------------
    # KEEP ONLY NUMERIC DATA FOR SAFETY
    # -------------------------------
    numeric_df = df.select_dtypes(include=['number'])

    print("\n📌 BASIC STATISTICS")
    print(numeric_df.describe())

    # -------------------------------
    # CORRELATION ANALYSIS
    # -------------------------------
    print("\n📌 FEATURE CORRELATION (Top 10 strongest with label)\n")

    corr = numeric_df.corr()["label"].sort_values(ascending=False)
    print(corr.head(10))

    # -------------------------------
    # VISUALIZATION
    # -------------------------------
    plt.figure()
    df["label"].value_counts().plot(kind="bar")
    plt.title("Phishing vs Legitimate Distribution")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.show()

    # -------------------------------
    # SAVE CLEANED VERSION
    # -------------------------------
    df.to_csv("data/processed/cleaned_dataset.csv", index=False)
    print("\n✅ Analysis complete & dataset saved")


if __name__ == "__main__":
    analyze_data()