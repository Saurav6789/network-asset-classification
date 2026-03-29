# 📊 Asset Classification & Data Quality Dashboard

This project focuses on **asset classification, data quality validation, and anomaly detection** using network fingerprint data (DHCP, OS, Vendor, etc.).  

It includes:
- Data enrichment & feature engineering  
- Error and inconsistency detection  
- Data Quality scoring  
- Interactive dashboard using Dash  

---

# 🚀 Project Structure
network-asset-classification/
│
├── app.py # Main entry point (run this file)
├── data_processing.py # Data cleaning & filtering logic
├── metrics.py # KPI calculations
├── callbacks.py # Dash callbacks
│
├── data/
│ └── data.csv # Raw dataset
│
├── dashboard_data/
│ └── dashboard_data.csv # Processed data for dashboard
│
├── Network_analysis.ipynb # Data exploration & feature engineering
├── pyproject.toml # Project dependencies
├── uv.lock # Dependency lock file
├── README.md


---

# ⚙️ Setup Instructions (Using uv)

## 1️⃣ Install uv (if not installed)

```bash
pip install uv

## Create Environment

uv venv

## Install Dependencies 

uv pip install -r pyproject.toml

## Running the app

python app.py

## Open In Browser

http://127.0.0.1:8051
