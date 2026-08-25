"""
Scenario 1: Data Loading and Cleaning
--------------------------------------
Steps:
1. Load the dataset
2. Display first 5 rows
3. Display column names
4. Check missing values
5. Handle missing values
6. Convert required columns to numeric
"""

import pandas as pd
import numpy as np

# ------------------------------------------------------------------
# 1. Load the dataset
# ------------------------------------------------------------------
# Replace 'your_file.csv' with your actual file path.
# Use pd.read_excel(...) instead if it's an Excel file.
file_path = "your_file.csv"
df = pd.read_csv(file_path)

# ------------------------------------------------------------------
# 2. Display first 5 rows
# ------------------------------------------------------------------
print("First 5 rows of the dataset:")
print(df.head())

# ------------------------------------------------------------------
# 3. Display column names
# ------------------------------------------------------------------
print("\nColumn names:")
print(df.columns.tolist())

# ------------------------------------------------------------------
# 4. Check missing values
# ------------------------------------------------------------------
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nPercentage of missing values per column:")
print((df.isnull().sum() / len(df)) * 100)

# ------------------------------------------------------------------
# 5. Handle missing values
# ------------------------------------------------------------------
# Choose ONE (or a combination) of the strategies below depending on
# your dataset. Common approaches:

# --- Option A: Drop rows with any missing values ---
# df = df.dropna()

# --- Option B: Drop columns that are mostly missing (e.g. >50% missing) ---
# threshold = 0.5
# df = df.loc[:, df.isnull().mean() < threshold]

# --- Option C: Fill numeric columns with mean/median ---
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# --- Option D: Fill categorical/text columns with mode (most frequent value) ---
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# Verify no missing values remain (or only in columns you intentionally left)
print("\nMissing values after handling:")
print(df.isnull().sum())

# ------------------------------------------------------------------
# 6. Convert required columns to numeric
# ------------------------------------------------------------------
# List the columns that SHOULD be numeric but might be stored as
# strings/objects (e.g. due to commas, currency symbols, stray text).
columns_to_convert = ["column1", "column2"]  # <-- update with your actual column names

for col in columns_to_convert:
    # Remove common non-numeric characters before conversion (optional)
    df[col] = df[col].astype(str).str.replace(",", "", regex=False)
    df[col] = df[col].astype(str).str.replace("$", "", regex=False)

    # Convert to numeric; invalid parsing becomes NaN instead of raising an error
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nData types after conversion:")
print(df.dtypes)

# ------------------------------------------------------------------
# Final check
# ------------------------------------------------------------------
print("\nCleaned dataset preview:")
print(df.head())

print("\nDataset shape:", df.shape)
