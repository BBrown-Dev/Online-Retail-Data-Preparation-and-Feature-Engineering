# Online Retail Data Preparation & Feature Engineering

A complete data‑science workflow for the Online Retail II dataset including exploratory data analysis (EDA), data cleaning, missing‑value handling, outlier detection, feature engineering, scaling, and preparation for downstream machine‑learning tasks.

---

## Project Overview
This project demonstrates a full data‑preparation pipeline using real customer transaction data. The workflow includes:

- Dataset ingestion  
- Exploratory data analysis (EDA)  
- Handling missing values  
- Outlier detection and removal  
- Creation of new engineered features  
- Normalization and scaling  
- Train/validation dataset splitting  

This repository is structured for clarity, reproducibility, and professional presentation.

---

## Key Features

### 1. Exploratory Data Analysis
- Summary statistics  
- Distribution plots  
- Boxplots for outlier detection  
- Variable type identification  

### 2. Data Cleaning
- Missing value imputation  
- Removal of invalid or inconsistent records  
- Handling negative quantities and zero‑price anomalies  

### 3. Feature Engineering
- `TotalValue` (Quantity &times; UnitPrice)  
- `InvoiceMonth` (Extracted from InvoiceDate)  
- `IsReturn` (Flag for negative quantities) 

### 4. Scaling & Normalization
- Min‑Max scaling applied to key numerical features  
- Preprocessing aligned with scikit‑learn best practices  

### 5. Train/Test Split
- 80/20 split for future modeling tasks  

---

## Technologies Used
- Python 3.14
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- scikit‑learn  

---

## Installation

Clone the repository:

```
git clone https://github.com/BBrown-Dev/Online-Retail-Data-Preparation-and-Feature-Engineering.git
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Project

From the project root:

```
python src/main.py
```

Ensure the dataset is located in:

```
data/online_retail_II.xlsx
```

---

## Dataset Source
The dataset used in this project is the Online Retail II dataset from the UCI Machine Learning Repository.

---

## License
This project is for educational and academic use.

---

## Acknowledgments
- UCI Machine Learning Repository  
- GeeksforGeeks tutorials on EDA, feature engineering, and normalization  
- Medium articles on data cleaning and outlier analysis  
