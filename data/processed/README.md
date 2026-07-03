# ⚙️ Processed Datasets
This directory contains clean, formatted datasets ready for model training and analysis.

## 📂 Directory Structure
* ```cleaned_dataset.csv``` — The initial processed dataset after data cleaning and formatting.

* ```features_dataset.csv``` — The final feature-engineered dataset used for model training.
  
## 📄 Data Format
* ```Type:``` CSV

* ```Structure of cleaned_dataset:``` Domain | Having_@_symbol	 | Having_IP | Path

## 🎯 Purpose
* Usage: Files here are the output of your ```data_processing``` modules.

* Consistency: These files are used as the primary input for the ```model_training``` and evaluation pipelines.
  
## 🚀 How It Works
* Writing: The processing scripts output cleaned_dataset.csv first, which is then transformed into the features_dataset.csv required for model input.

* Reading: The model_training.py and evaluate_model.py modules consume features_dataset.csv to perform their analysis.
  
## ⚠️ Maintenance
These files are generated automatically. If you update your ```data_processing``` logic, you may need to delete the contents of this folder and re-run your scripts to generate fresh, updated data.
