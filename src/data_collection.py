import os
import pandas as pd


def execute_task_1_collection():
    print("🚀 Starting Task 1: Secure Data Collection & Sourcing...")

    # Secure, verified cybersecurity benchmark dataset link
    secure_data_url = "https://raw.githubusercontent.com/shreyagopal/Phishing-Website-Detection-by-Machine-Learning-Techniques/master/DataFiles/5.urldata.csv"

    print("📥 Stream-downloading raw unified feature matrix...")
    try:
        # Read the raw data stream
        df_raw = pd.read_csv(secure_data_url)

        # Enforce directory layout guidelines
        raw_storage_dir = "data/raw"
        os.makedirs(raw_storage_dir, exist_ok=True)

        print("✂️ Splitting dataset into separate phishing and legitimate matrices...")

        # Filter rows where Label is 1 (Phishing) and drop the tracking column if desired
        df_phishing = df_raw[df_raw['Label'] == 1]
        phishing_path = os.path.join(raw_storage_dir, "phishing.csv")
        df_phishing.to_csv(phishing_path, index=False)

        # Filter rows where Label is 0 (Legitimate)
        df_legitimate = df_raw[df_raw['Label'] == 0]
        legitimate_path = os.path.join(raw_storage_dir, "legitimate.csv")
        df_legitimate.to_csv(legitimate_path, index=False)

        print("\n📥 Data Successfully Collected and Separated!")
        print(f"   ↳ 🚨 Saved {df_phishing.shape[0]} phishing rows to: {phishing_path}")
        print(f"   ↳ ✅ Saved {df_legitimate.shape[0]} legitimate rows to: {legitimate_path}")
        print("✅ Task 1 Data Sourcing Complete.")

    except Exception as e:
        print(f"❌ Network collection failed. Check connection parameters: {e}")


if __name__ == "__main__":
    execute_task_1_collection()