import os
import pandas as pd
import numpy as np


def execute_task3_secure_storage():
    print("==================================================")
    print("      TASK 3: SECURE DATA STORAGE ENGINE         ")
    print("==================================================")

    raw_dir = "data/raw"
    processed_dir = "data/processed"
    os.makedirs(processed_dir, exist_ok=True)

    phishing_path = os.path.join(raw_dir, "phishing.csv")
    legitimate_path = os.path.join(raw_dir, "legitimate.csv")

    if not os.path.exists(phishing_path) or not os.path.exists(legitimate_path):
        print("[-] Error: Missing raw dataset assets. Run collection first.")
        return

    # Load raw sources
    df_phish = pd.read_csv(phishing_path)
    df_legit = pd.read_csv(legitimate_path)
    df = pd.concat([df_phish, df_legit], ignore_index=True)

    print(f"[*] Initial ingested rows: {df.shape[0]}")

    # --- ENFORCE SCHEMA CONSTRAINTS ---
    # 1. Enforce Non-Nullability (No missing data allowed)
    df = df.dropna(subset=['Domain', 'Label'])

    # 2. Enforce Numeric Datatypes on feature columns
    feature_cols = [col for col in df.columns if col not in ['Domain']]
    for col in feature_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop any records that failed formatting verification
    df = df.dropna()

    # 3. Enforce Binary Value Range Constraints (Domain Integrity Rule)
    binary_cols = [col for col in feature_cols if col not in ['URL_Depth', 'Label']]
    for col in binary_cols:
        # Keep only rows where value is strictly 0 or 1
        df = df[df[col].isin([0, 1])]

    # 4. Enforce Entity Integrity (Unique Domains, clear duplicates)
    df = df.drop_duplicates(subset=['Domain'])

    print(f"[*] Schema validation complete.")
    print(f"[*] Total valid structured records to be stored: {df.shape[0]}")

    # Save the finalized, schema-compliant clean master dataset
    output_master_path = os.path.join(processed_dir, "cleaned_master_dataset.csv")
    df.to_csv(output_master_path, index=False)

    # Generate formal Task 3 Storage Documentation report
    storage_log_path = os.path.join(processed_dir, "storage_documentation.txt")
    with open(storage_log_path, "w", encoding="utf-8") as f:
        f.write("==================================================\n")
        f.write("          DATA STORAGE IMPLEMENTATION LOG         \n")
        f.write("==================================================\n")
        f.write(f"Storage Format       : Structured CSV Layout\n")
        f.write(f"Master Export Path   : {output_master_path}\n")
        f.write(f"Final Record Count   : {df.shape[0]} unique rows\n")
        f.write(f"Total Column Features: {df.shape[1]} attributes\n")
        f.write(f"Integrity Check      : PASSED (Zero Nulls, Enforced Binaries)\n")

    print(f"[+] Task 3 Deliverable successfully persisted: {output_master_path}")
    print(f"[+] Storage Documentation generated: {storage_log_path}")


if __name__ == "__main__":
    execute_task3_secure_storage()