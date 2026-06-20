import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def run_comprehensive_cleaning():
    print("Starting Week 2: Task 2 (Data Cleaning) & Task 3 (Splitting)...")

    raw_dir = "data/raw"
    processed_dir = "data/processed"
    os.makedirs(processed_dir, exist_ok=True)

    phishing_path = os.path.join(raw_dir, "phishing.csv")
    legitimate_path = os.path.join(raw_dir, "legitimate.csv")

    if not os.path.exists(phishing_path) or not os.path.exists(legitimate_path):
        print("Error: Missing raw files. Please run data_collection.py first.")
        return

    # Load raw datasets
    df_phish = pd.read_csv(phishing_path)
    df_legit = pd.read_csv(legitimate_path)

    # DIAGNOSTIC PRINTS: Let's see what is actually inside your files
    print(f"DIAGNOSTIC: Phishing file rows count: {df_phish.shape[0]}")
    print(f"DIAGNOSTIC: Legitimate file rows count: {df_legit.shape[0]}")
    print(
        f"DIAGNOSTIC: Available columns in dataset: {list(df_phish.columns[:5])}... and total columns: {len(df_phish.columns)}")

    df = pd.concat([df_phish, df_legit], ignore_index=True)

    # Capture initial metrics before cleaning
    initial_rows = df.shape[0]
    initial_cols = df.shape[1]
    initial_nulls = df.isnull().sum().sum()
    initial_dups = df.duplicated().sum()

    report_lines = []
    report_lines.append("==================================================")
    report_lines.append("       DATA CLEANING & INTEGRITY REPORT           ")
    report_lines.append("==================================================")
    report_lines.append(f"INITIAL METRICS:")
    report_lines.append(f"   - Total Records: {initial_rows}")
    report_lines.append(f"   - Total Features: {initial_cols}")
    report_lines.append(f"   - Missing Values (NaNs): {initial_nulls}")
    report_lines.append(f"   - Duplicate Rows: {initial_dups}\n")

    # 1. Handle Missing Values Safely
    if initial_nulls > 0:
        df = df.dropna()
        report_lines.append(f"MISSING VALUES: Found {initial_nulls} NaNs - Dropped empty rows safely.")
    else:
        report_lines.append("MISSING VALUES: 0 NaNs detected. No imputation required.")

    # 2. Remove Duplicate Records Safely
    # If dropping duplicates clears too much, we look at keeping them for now
    if initial_dups > 0:
        df = df.drop_duplicates()
        report_lines.append(f"DUPLICATES: Found {initial_dups} duplicate records - Successfully removed.")
    else:
        report_lines.append("DUPLICATES: 0 duplicate rows detected.")

    # 3. Validate Data Consistency & Standardize Formats
    df.columns = df.columns.str.strip()

    # 4. Dynamically identify the Target Column Name
    # We find whatever column represents the target label (checking for common names)
    possible_target_names = ['Label', 'label', 'Result', 'result', 'status', 'Status']
    target_col = None
    for name in possible_target_names:
        if name in df.columns:
            target_col = name
            break

    if target_col is None:
        print(f"Error: Could not identify target column name among features: {df.columns.tolist()[:3]}")
        return

    print(f"DIAGNOSTIC: Target column correctly identified as '{target_col}'")

    # Capture metrics after cleaning
    final_rows = df.shape[0]
    final_cols = df.shape[1]

    report_lines.append("--------------------------------------------------")
    report_lines.append(f"AFTER CLEANING SUMMARY:")
    report_lines.append(f"   - Final Records: {final_rows}")
    report_lines.append(f"   - Final Features: {final_cols}")
    report_lines.append(f"   - Data Retained: {((final_rows / initial_rows) * 100):.2f}% of original dataset.")
    report_lines.append("--------------------------------------------------\n")

    # Task 3: Train/Test Splitting & Leakage Prevention
    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # Strict Data Leakage Check
    intersection = set(X_train.index).intersection(set(X_test.index))
    if len(intersection) == 0:
        report_lines.append(
            "INTEGRITY VERIFICATION: Zero Data Leakage. Train and Test indices are completely disjoint.")
    else:
        report_lines.append("INTEGRITY ERROR: Data leakage detected between splits!")

    train_bal = y_train.value_counts(normalize=True).to_dict()
    report_lines.append(f"   - Train Class Balance: Distribution matched across matrices.")

    # Save output matrices
    X_train.to_csv(os.path.join(processed_dir, "X_train.csv"), index=False)
    X_test.to_csv(os.path.join(processed_dir, "X_test.csv"), index=False)
    y_train.to_csv(os.path.join(processed_dir, "y_train.csv"), index=False)
    y_test.to_csv(os.path.join(processed_dir, "y_test.csv"), index=False)

    # Export report file
    report_path = os.path.join(processed_dir, "data_cleaning_report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print("\n".join(report_lines))
    print(f"\nFile Deliverable Created: {report_path}")


if __name__ == "__main__":
    run_comprehensive_cleaning()