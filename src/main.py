"""
Online Retail Data Preparation & Feature Engineering
Author: Bruce Brown
Description:
    This script performs exploratory data analysis (EDA), data cleaning,
    outlier handling, feature engineering, scaling, and dataset splitting
    using the Online Retail II dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import os
from pathlib import Path


# Get the script's directory and construct paths relative to it
script_dir = Path(__file__).parent.parent
data_file = script_dir / "data" / "online_retail_II.xlsx"
figures_dir = script_dir / "reports" / "figures"

# Load Data
df = pd.read_excel(data_file)

print("\nDataset Loaded Successfully")
print(df.head())

# Start Basic Exploratory Data Analysis (EDA)
print("\nDataset Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# Identify Variable Types
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object', 'string']).columns

print("\nNumerical Columns:", list(numerical_cols))
print("Categorical Columns:", list(categorical_cols))

# Histograms
df[numerical_cols].hist(figsize=(12, 8))
plt.suptitle("Distribution of Numerical Variables")
plt.tight_layout()
plt.savefig(figures_dir / "histograms.png")
plt.close()

# Boxplots
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[numerical_cols])
plt.title("Boxplot of Numerical Features")
plt.tight_layout()
plt.savefig(figures_dir / "boxplots.png")
plt.close()

# Start Data Cleaning
print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# Handle missing CustomerID by imputing with -1
df['Customer ID'] = df['Customer ID'].fillna(-1)

# Remove rows missing Description (cannot analyze product without description)
df = df.dropna(subset=['Description'])

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# Outlier Handling
# Remove extreme negative quantities (beyond normal returns)
df = df[df['Quantity'] > -50]

# Remove zero or negative prices
df = df[df['Price'] > 0]

# Start Feature Engineering
# Feature 1: Total transaction value
df['TotalValue'] = df['Quantity'] * df['Price']

# Feature 2: Invoice month (seasonality)
df['InvoiceMonth'] = df['InvoiceDate'].dt.month

# Feature 3: Return flag
df['IsReturn'] = df['Quantity'].apply(lambda x: 1 if x < 0 else 0)

print("\nNew Features Added")
print(df[['TotalValue', 'InvoiceMonth', 'IsReturn']].head())

# Start Scaling / Normalization
scaler = MinMaxScaler()

df[['Quantity_scaled', 'Price_scaled', 'TotalValue_scaled']] = scaler.fit_transform(
    df[['Quantity', 'Price', 'TotalValue']]
)

print("\nScaled Feature Samples")
print(df[['Quantity_scaled', 'Price_scaled', 'TotalValue_scaled']].head())

# Start Train / Validation Split
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

print("\nTraining Set Shape:", train_df.shape)
print("Validation Set Shape:", test_df.shape)

# Completion Notifications
print("\n=== Data Preparation Complete ===")
print("Figures saved to: reports/figures/")
print("Ready for modeling or further analysis.")