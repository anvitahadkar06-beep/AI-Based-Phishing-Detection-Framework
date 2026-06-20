# ⚙️ Source Code

This folder contains all the production Python modules, data scripts, and machine learning model code for the phishing framework.

## 📂 Core Script Architecture

- **`data_collection.py`**: Ingests raw phishing and legitimate URL datasets, initializing the initial framework pipeline.
- **`data_processing.py`**: Standardizes variable labels, handles deduplication, logs structure completeness, and partitions features into stratified train/test matrices.
- **`data_storage.py`**: Reads validation rules directly from the system schema blueprint, running strict typing constraints to prevent data leakage before storage.

## 🚀 Script Invocations

To run the pipeline modules sequentially, execute them from your terminal at the project root level:

```bash
# Step 1: Execute ingestion and profiling
python src/data_processing.py

# Step 2: Enforce data constraints and output verified matrices
python src/data_storage.py
```
