# 📊 Data Collection

This directory houses the datasets used to train, validate, and test the AI-Based Phishing Detection Framework.

## 📂 Directory Layout

- **`raw/`**: Contains the original, unaltered data source files (`phishing.csv`, `legitimate.csv`). These files are treated as read-only to preserve data lineage.
- **`processed/`**: Holds the engineered, schema-validated files ready for model consumption (`X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`).
- **`data_schema_design.txt`**: The engineering blueprint defining data types, structural constraints, and non-nullability fields.

## 🛠️ Data Schema & Integrity Rules

Data integrity is enforced dynamically by the storage engine using the structural constraints defined in `data_schema_design.txt`. 

### Key Constraints Enforced:
1. **Type & Bounds Match**: Features must perfectly map to specified data types (e.g., URL length integers, binary flags).
2. **Nullability Checks**: Structural columns are strictly validated against unexpected missing (`NaN`) values.
3. **Disjoint Matrix Verification**: Train and test index checks guarantee **zero data leakage** prior to modeling.
