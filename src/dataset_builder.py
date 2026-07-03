"""
==================================================
AI Based Phishing Detection Framework

Dataset Builder

Reads the master dataset and generates a new
feature dataset using feature_extraction.py
==================================================
"""

import pandas as pd

from feature_extraction import extract_features


# ---------------------------------------------
# Paths
# ---------------------------------------------

INPUT_DATASET = "data/processed/master_dataset.csv"

OUTPUT_DATASET = "data/processed/features_dataset.csv"


# ---------------------------------------------
# Build Dataset
# ---------------------------------------------

def build_dataset():

    print("=" * 60)
    print("Loading Dataset...")
    print("=" * 60)

    df = pd.read_csv(INPUT_DATASET)

    print("Rows :", len(df))
    print("Columns :", len(df.columns))

    # -----------------------------------------

    if "Domain" in df.columns:

        url_column = "Domain"

    elif "url" in df.columns:

        url_column = "url"

    else:

        raise Exception(
            "No URL column found. Expected 'Domain' or 'url'."
        )

    print("\nUsing URL Column :", url_column)

    # -----------------------------------------

    feature_rows = []

    total = len(df)

    print("\nExtracting Features...\n")

    for index, row in df.iterrows():

        url = str(row[url_column])

        label = row["label"]

        try:

            features = extract_features(url)

            features["label"] = label

            feature_rows.append(features)

        except Exception as e:

            print(f"Skipped row {index} : {e}")

        if (index + 1) % 100 == 0:

            print(f"Processed {index+1}/{total}")

    # -----------------------------------------

    feature_df = pd.DataFrame(feature_rows)

    feature_df.to_csv(OUTPUT_DATASET, index=False)

    print("\nDataset Created Successfully")

    print(feature_df.head())

    print()

    print("Shape :", feature_df.shape)

    print()

    print("Saved to")

    print(OUTPUT_DATASET)


# ---------------------------------------------

if __name__ == "__main__":

    build_dataset()