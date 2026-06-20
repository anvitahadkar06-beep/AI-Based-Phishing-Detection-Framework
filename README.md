<img width="2125" height="575" alt="github-header-banner (2)" src="https://github.com/user-attachments/assets/3349eb70-be5c-495e-a384-46c81df44cc9" />

## 🛡️ Project Description

Phishing attacks are among the most common cybersecurity threats, often leading to credential theft, financial fraud, and data breaches. As attackers continue to develop more sophisticated phishing techniques, traditional detection methods may not always be sufficient. This project aims to leverage Machine Learning and Cybersecurity techniques to identify phishing websites and improve online security through automated detection.

## 📂 Project Structure

```
AI-Based-Phishing-Detection-Framework/
├── README.md                      # Main project overview and banner
├── 📁 reports/                  
│   └── README.md                  # Documentation for weekly and final reports
├── 📁 data/
│   └── raw/                       # Unaltered source files (phishing.csv, legitimate.csv)
│   └── processed/                 # Validated master datasets and stratified train/test splits
│   └── data_schema_design.txt     # Data type blueprints and structural constraints   
│   └── README.md                  # Documentation for data collection & datasets
├── 📁 src/
│   └── data_collection.py         # Source ingestion pipelines
│   └── data_processing.py         # Data cleansing and partition layout engine
│   └── data_storage.py            # Secure schema validation and storage engine           
│   └── README.md                  # Documentation for core source code & ML models
├── 📁 deployment/                  
│   └── README.md                  # Deployment configs and operational instructions
```

## 🛠️ Tech Stack

* Python
* Machine Learning
* Cybersecurity

## 🚀 How to Run

### 1. Install Dependencies
Navigate into your project root directory and install the required data science and machine learning packages:
```bash
cd AI-Based-Phishing-Detection-Framework
pip install pandas numpy scikit-learn
```
(Alternatively, if you are utilizing a requirements tracking file, run: pip install -r requirements.txt)

2. Configure File Ingestion Routes
Open src/data_collection.py and verify your input file paths inside your loading functions to ensure they point securely to your source datasets:

Python
# Ensure these match the exact filenames inside your data/raw/ directory
phishing_data_path = "data/raw/phishing.csv" 
legitimate_data_path = "data/raw/legitimate.csv"
Format constraint: Raw source files must be placed inside the data/raw/ directory prior to pipeline execution.

3. Configure Schema Rules
Open data/data_schema_design.txt to modify or append structural constraints, data types, or non-nullability fields that your data storage engine must enforce:

Plaintext
# Data Schema Blueprint Guidelines:
url_length: int (NonNull)
is_phishing: int (Binary: 0 or 1)
4. Execute the Data Pipeline
Run the modular execution scripts sequentially from the project root directory to clean the data, generate stratified splits, validate schemas, and securely store the outputs:

Bash
# Step 1: Clean, profile, and split your source datasets
python src/data_processing.py

# Step 2: Enforce strict schema validation rules and securely store features
python src/data_storage.py
5. Review Generated Artifacts
Once execution completes successfully, navigate to your local output directories to review your production-ready tracking assets:

Processed Splits: data/processed/X_train.csv, X_test.csv, y_train.csv, y_test.csv

Data Integrity Summaries: data/processed/data_cleaning_report.txt and storage_documentation.txt

## 👥 Contributors

* Anvita Hadkar
* Pranjali Mahadik
* Siddhi Gudhekar
