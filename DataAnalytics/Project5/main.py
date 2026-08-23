# ============================================================
#                 SCENARIO 1
#          Data Loading & Basic Cleaning
# ============================================================
 
# ------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
 
# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------
 
df = pd.read_csv("cardata.csv")
 
print("=" * 60)
print("CARS DATA ANALYSIS - SCENARIO 1")
print("=" * 60)
 
 
# ------------------------------------------------------------
# 3. DISPLAY FIRST 5 ROWS
# ------------------------------------------------------------
 
print("\nFIRST 5 ROWS:")
print(df.head())
 
 
# ------------------------------------------------------------
# 4. DISPLAY LAST 5 ROWS
# ------------------------------------------------------------
 
print("\nLAST 5 ROWS:")
print(df.tail())
 
 
# ------------------------------------------------------------
# 5. DISPLAY COLUMN NAMES
# ------------------------------------------------------------
 
print("\nCOLUMN NAMES:")
print(df.columns)
 
 
# ------------------------------------------------------------
# 6. DISPLAY SHAPE OF DATASET
# ------------------------------------------------------------
 
print("\nSHAPE OF DATASET:")
print(df.shape)
 
 
# ------------------------------------------------------------
# 7. CHECK DATA TYPES
# ------------------------------------------------------------
 
print("\nDATA TYPES:")
print(df.dtypes)
 
 
# ------------------------------------------------------------
# 8. CHECK MISSING VALUES
# ------------------------------------------------------------
 
print("\nMISSING VALUES:")
print(df[
    [
        "Selling_Price",
        "Present_Price",
        "Kms_Driven",
        "Fuel_Type"
    ]
].isnull().sum())
 
 
# ------------------------------------------------------------
# 9. CONVERT NUMERIC COLUMNS TO NUMERIC TYPE
# ------------------------------------------------------------
 
df["Selling_Price"] = pd.to_numeric(
    df["Selling_Price"],
    errors="coerce"
)
 
df["Present_Price"] = pd.to_numeric(
    df["Present_Price"],
    errors="coerce"
)
 
df["Kms_Driven"] = pd.to_numeric(
    df["Kms_Driven"],
    errors="coerce"
)
 
df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
)
 
 
# ------------------------------------------------------------
# 10. HANDLE MISSING VALUES
# ------------------------------------------------------------
 
# Numeric columns → Mean
 
df["Selling_Price"] = df["Selling_Price"].fillna(
    df["Selling_Price"].mean()
)
 
df["Present_Price"] = df["Present_Price"].fillna(
    df["Present_Price"].mean()
)
 
df["Kms_Driven"] = df["Kms_Driven"].fillna(
    df["Kms_Driven"].mean()
)
 
 
# Categorical column → Mode
 
df["Fuel_Type"] = df["Fuel_Type"].fillna(
    df["Fuel_Type"].mode()[0]
)
 
 
# ------------------------------------------------------------
# 11. CONVERT SELLING PRICE TO NUMPY ARRAY
# ------------------------------------------------------------
 
selling_price_array = df["Selling_Price"].to_numpy()
 
 
# ------------------------------------------------------------
# 12. CONVERT KMS DRIVEN TO NUMPY ARRAY
# ------------------------------------------------------------
 
kms_driven_array = df["Kms_Driven"].to_numpy()
 
 
# ------------------------------------------------------------
# 13. NUMPY CALCULATIONS
# ------------------------------------------------------------
 
minimum_selling_price = np.min(selling_price_array)
 
maximum_selling_price = np.max(selling_price_array)
 
average_selling_price = np.mean(selling_price_array)
 
 
# ------------------------------------------------------------
# 14. DISPLAY RESULTS
# ------------------------------------------------------------
 
print("\n" + "=" * 60)
print("NUMPY CALCULATIONS")
print("=" * 60)
 
print("\nMinimum Selling Price:",
      minimum_selling_price)
 
print("Maximum Selling Price:",
      maximum_selling_price)
 
print("Average Selling Price:",
      average_selling_price)
 
 
# ------------------------------------------------------------
# 15. FINAL MISSING VALUE CHECK
# ------------------------------------------------------------
 
print("\nFINAL MISSING VALUE CHECK:")
print(
    df[
        [
            "Selling_Price",
            "Present_Price",
            "Kms_Driven",
            "Fuel_Type"
        ]
    ].isnull().sum()
)
 
 
# ------------------------------------------------------------
# 16. FINAL MESSAGE
# ------------------------------------------------------------
 
print("\n" + "=" * 60)
print("SCENARIO 1 COMPLETED SUCCESSFULLY")
print("=" * 60)
 
# ============================================================
#                 SCENARIO 2
#             Selling Price Trend
#                 Line Graph
# ============================================================
 
print("\n" + "=" * 60)
print("SCENARIO 2: SELLING PRICE TREND")
print("=" * 60)
 
 
# ------------------------------------------------------------
# 1. SELECT REQUIRED COLUMNS
# ------------------------------------------------------------
 
sample = df[["Car_Name", "Selling_Price"]]
 
 
# ------------------------------------------------------------
# 2. TAKE FIRST 10 ROWS
# ------------------------------------------------------------
 
sample = sample.head(10)
 
print("\nFIRST 10 CARS:")
print(sample)
 
 
# ------------------------------------------------------------
# 3. CONVERT SELLING PRICE INTO NUMPY ARRAY
# ------------------------------------------------------------
 
selling_price_array = sample["Selling_Price"].to_numpy()
 
print("\nSELLING PRICE NUMPY ARRAY:")
print(selling_price_array)
 
 
# ------------------------------------------------------------
# 4. CREATE X-AXIS VALUES
# ------------------------------------------------------------
 
x_values = np.arange(len(selling_price_array))
 
print("\nX-AXIS VALUES:")
print(x_values)
 
 
# ------------------------------------------------------------
# 5. CREATE LINE GRAPH
# ------------------------------------------------------------
 
plt.figure(figsize=(10, 5))
 
plt.plot(
    x_values,
    selling_price_array,
    marker="o"
)
 
 
# ------------------------------------------------------------
# 6. ADD TITLE AND LABELS
# ------------------------------------------------------------
 
plt.title("Selling Price Trend (First 10 Cars)")
 
plt.xlabel("Row Index")
 
plt.ylabel("Selling Price")
 
 
# ------------------------------------------------------------
# 7. ADD GRID
# ------------------------------------------------------------
 
plt.grid(True)
 
 
# ------------------------------------------------------------
# 8. SAVE GRAPH
# ------------------------------------------------------------
 
plt.savefig(
    "Graphs/selling_price_line.png",
    bbox_inches="tight"
)
 
 
# ------------------------------------------------------------
# 9. DISPLAY GRAPH
# ------------------------------------------------------------
 
plt.show()
 
plt.close()
 
 
# ------------------------------------------------------------
# 10. SUCCESS MESSAGE
# ------------------------------------------------------------
 
print("\nScenario 2 graph saved successfully.")
 
print("=" * 60)
print("SCENARIO 2 COMPLETED SUCCESSFULLY")
print("=" * 60)

'''
=================================================================================================================================
                                     🟡 SCENARIO 3: Expensive Cars Analysis (Filtering + Bar)
=================================================================================================================================
�� Tasks:
● Filter cars where:
○ Selling_Price > 10
● Group the filtered data by:
○ Fuel_Type
● Count number of cars in each fuel type.
● Convert:
○ fuel type labels
○ counts
into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Fuel Type
○ Y-axis → Count of expensive cars
● Add:
○ title
○ x-label
○ y-label
● Save the graph.

'''
expensive_cars = df[df['Selling_Price'] > 10]
fuel_counts = expensive_cars.groupby('Fuel_Type').size()
fuel_labels = np.array(fuel_counts.index)
fuel_values = np.array(fuel_counts.values)
plt.bar(fuel_labels, fuel_values, color='skyblue')
plt.title("Fuel Types of Expensive Cars")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig("Graphs/expensive_car_analysis.png")
plt.show()

'''
=================================================================================================================================
                                     🟡 SCENARIO 4: Pie Chart (Fuel Type Distribution) + Save
=================================================================================================================================
�� Tasks:
● Count the number of cars in each:
○ Fuel_Type
● Select all categories or top categories if needed.
● Prepare:
○ labels
○ values
● Convert values into a NumPy array.
● Plot a pie chart using Matplotlib.
● Add:
○ percentage labels
○ title
● Save the graph.

'''
counts = df['Fuel_Type'].value_counts()
labels = counts.index
values = np.array(counts.values)  
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Overall Fuel Type Distribution")
plt.savefig("Graphs/fuel_type_distribution.png")

# ------------------------------------------------------------------
# Scenario 5: Present Price vs Selling Price (Scatter Plot)
# ------------------------------------------------------------------

# Select relevant columns
scatter_df = df[["Present_Price", "Selling_Price"]].copy()

# Remove missing values if any
scatter_df = scatter_df.dropna()

# Take a smaller sample (first 100 rows)
scatter_sample = scatter_df.head(100)

# Convert both columns into NumPy arrays
present_price_arr = scatter_sample["Present_Price"].to_numpy()
selling_price_arr = scatter_sample["Selling_Price"].to_numpy()

# Plot scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(present_price_arr, selling_price_arr, color="teal", alpha=0.7)
plt.title("Present Price vs Selling Price")
plt.xlabel("Present Price (in Lakhs)")
plt.ylabel("Selling Price (in Lakhs)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("Graphs/present_vs_selling_price_scatter.png")

# Observation: A positive relationship generally means cars with a higher
# present (original) price also tend to sell at a higher price.
correlation = np.corrcoef(present_price_arr, selling_price_arr)[0, 1]
print(f"Correlation between Present Price and Selling Price: {correlation:.2f}")
if correlation > 0:
    print("Observation: There is a positive relationship between Present Price and Selling Price.")
else:
    print("Observation: There is a negative relationship between Present Price and Selling Price.")


# ------------------------------------------------------------------
# Scenario 6: Car Age Category Analysis + Bar Chart
# ------------------------------------------------------------------

def categorize_age(year):
    if year >= 2015:
        return "New"
    elif 2010 <= year <= 2014:
        return "Medium"
    else:
        return "Old"

# Create new column
df["Car Age Category"] = df["Year"].apply(categorize_age)

# Count number of cars in each category
age_category_counts = df["Car Age Category"].value_counts()

# Convert category names and counts into NumPy arrays
category_labels = age_category_counts.index.to_numpy()
category_counts = age_category_counts.values

# Plot bar chart
plt.figure(figsize=(7, 5))
plt.bar(category_labels, category_counts, color=["#4CAF50", "#FFC107", "#F44336"])
plt.title("Car Count by Age Category")
plt.xlabel("Car Age Category")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.savefig("Graphs/car_age_category_bar.png")


# ------------------------------------------------------------------
# Scenario 7: Kms Driven Distribution (Histogram)
# ------------------------------------------------------------------

# Select column and convert to NumPy array
kms_driven_arr = df["Kms_Driven"].to_numpy()

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(kms_driven_arr, bins=20, color="steelblue", edgecolor="black")
plt.title("Distribution of Kms Driven")
plt.xlabel("Kms Driven")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Graphs/kms_driven_histogram.png")

# Observation
median_kms = np.median(kms_driven_arr)
if df["Kms_Driven"].skew() > 0:
    print(f"Observation: The distribution is right-skewed (median = {median_kms:.0f} km); "
          f"most cars have lower mileage with a few high-mileage outliers.")
else:
    print(f"Observation: The distribution is fairly balanced (median = {median_kms:.0f} km).")

 
# Scenario 8
# Group by Transmission and calculate average Selling_Price
avg_price = df.groupby("Transmission")["Selling_Price"].mean()

# Convert into NumPy arrays
transmission_array = np.array(avg_price.index)
price_array = np.array(avg_price.values)

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(transmission_array, price_array)

# Add title and labels
plt.title("Average Selling Price by Transmission")
plt.xlabel("Transmission")
plt.ylabel("Average Selling Price")

# Save graph
plt.savefig("Graphs/transmission_selling_price.png")



# ------------------------------
# COUNT SELLER TYPES
# ------------------------------
seller_counts = df["Seller_Type"].value_counts().sort_values(ascending=False)

# Convert to NumPy
seller_labels = seller_counts.index.to_numpy()
seller_values = seller_counts.values

# ------------------------------
# BAR CHART (Clean & Colorful)
# ------------------------------
plt.figure(figsize=(8,5))

plt.bar(seller_labels, seller_values, color=["#4CAF50", "#2196F3", "#FF9800"])

plt.title("Seller Type Distribution", fontsize=14)
plt.xlabel("Seller Type", fontsize=12)
plt.ylabel("Number of Cars", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("Graphs/seller_type_bar.png")
plt.show()


# ------------------------------
# PIE CHART
# ------------------------------
plt.figure(figsize=(6,6))

plt.pie(
    seller_values,
    labels=seller_labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=["#FF6F61", "#6B5B95", "#88B04B"],
    textprops={'fontsize': 11}
)

plt.title("Seller Type Distribution (Pie Chart)", fontsize=14)

plt.tight_layout()
plt.savefig("Graphs/seller_type_pie.png")
plt.show()


# ------------------------------
# PART 1: FEATURE CREATION
# ------------------------------
df["Price_Difference"] = df["Present_Price"] - df["Selling_Price"]

# ------------------------------
# PART 2: NUMPY CALCULATIONS
# ------------------------------
selling_np = df["Selling_Price"].to_numpy()
price_diff_np = df["Price_Difference"].to_numpy()

price_change = np.diff(selling_np)

avg_depreciation = np.mean(price_diff_np)
max_depreciation = np.max(price_diff_np)
min_depreciation = np.min(price_diff_np)

print("\nAverage Depreciation:", avg_depreciation)
print("Maximum Depreciation:", max_depreciation)
print("Minimum Depreciation:", min_depreciation)


# ------------------------------
# PART 3: VISUALIZATIONS
# ------------------------------

# -------- 1. LINE GRAPH (Meaningful Trend) --------
year_avg = df.groupby("Year")["Selling_Price"].mean().sort_index()

plt.figure(figsize=(10,5))

plt.plot(year_avg.index, year_avg.values, marker='o', color="#E91E63")

plt.title("Average Selling Price by Year", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Selling Price", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("Graphs/year_trend.png")
plt.show()


# -------- 2. BAR CHART (Fuel Type Insight) --------
fuel_avg = df.groupby("Fuel_Type")["Selling_Price"].mean().sort_values()

plt.figure(figsize=(8,5))

fuel_avg.plot(kind='bar', color="#3F51B5")

plt.title("Average Selling Price by Fuel Type", fontsize=14)
plt.xlabel("Fuel Type", fontsize=12)
plt.ylabel("Average Selling Price", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("Graphs/fuel_bar.png")
plt.show()


# -------- 3. BAR CHART (Transmission Insight) --------
trans_avg = df.groupby("Transmission")["Selling_Price"].mean().sort_values()

plt.figure(figsize=(8,5))

trans_avg.plot(kind='bar', color="#009688")

plt.title("Average Selling Price by Transmission", fontsize=14)
plt.xlabel("Transmission", fontsize=12)
plt.ylabel("Average Selling Price", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("Graphs/transmission_bar.png")
plt.show()


# -------- 4. HISTOGRAM (Clean Distribution) --------
plt.figure(figsize=(8,5))

plt.hist(selling_np, bins=20, color="#FF5722", edgecolor='black')

plt.title("Selling Price Distribution", fontsize=14)
plt.xlabel("Selling Price", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("Graphs/selling_hist.png")
plt.show()


# ------------------------------
# PART 4: INSIGHTS
# ------------------------------
highest_fuel = fuel_avg.idxmax()
highest_trans = trans_avg.idxmax()

median_price = np.median(selling_np)

df["Car_Age"] = 2025 - df["Year"]
corr = df["Car_Age"].corr(df["Selling_Price"])

print("\nINSIGHTS:")
print("Fuel Type with Highest Avg Selling Price:", highest_fuel)
print("Transmission with Highest Avg Selling Price:", highest_trans)

if median_price < np.mean(selling_np):
    print("Most cars are concentrated in lower price range.")
else:
    print("Most cars are concentrated in higher price range.")

if corr < 0:
    print("Older cars tend to have lower selling prices.")
else:
    print("No strong negative relation between age and price.")