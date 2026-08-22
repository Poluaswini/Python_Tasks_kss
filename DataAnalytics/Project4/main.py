import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os        
 
# ==========================================
# SCENARIO 1: DATA LOADING & BASIC CLEANING
# ==========================================
 
# Task 1: Load dataset
df = pd.read_csv("kc_house_data.csv")
 
# Task 2: Display first 5 rows
print("First 5 Rows:")
print(df.head())
 
# Display column names
print("\nColumn Names:")
print(df.columns)
 
# Task 3: Check missing values
print("\nMissing Values Before Filling:")
 
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())
 
# Task 4: Convert columns to numeric
df["bedrooms"] = pd.to_numeric(
    df["bedrooms"],
    errors="coerce"
)
 
df["bathrooms"] = pd.to_numeric(
    df["bathrooms"],
    errors="coerce"
)
 
df["sqft_living"] = pd.to_numeric(
    df["sqft_living"],
    errors="coerce"
)
 
df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)
 
# Task 5: Fill missing values
 
# bedrooms → mode
df["bedrooms"] = df["bedrooms"].fillna(
    df["bedrooms"].mode()[0]
)
 
# bathrooms → mean
df["bathrooms"] = df["bathrooms"].fillna(
    df["bathrooms"].mean()
)
 
# sqft_living → mean
df["sqft_living"] = df["sqft_living"].fillna(
    df["sqft_living"].mean()
)
 
# price → mean
df["price"] = df["price"].fillna(
    df["price"].mean()
)
 
# Final missing-value check
print("\nMissing Values After Filling:")
 
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())
 
print("\nScenario 1 completed successfully!")
 
# ==========================================
# SCENARIO 2: LINE GRAPH + SAVE
# ==========================================
 
# Task 1 & 2: Select id and price, first 10 rows
line_df = df[["id", "price"]].head(10)
 
print("\nFirst 10 House Prices:")
print(line_df)
 
# Task 3: Convert price to NumPy array
price_array = line_df["price"].to_numpy()
 
print("\nPrice NumPy Array:")
print(price_array)
 
# Task 4: Create line graph
plt.figure(figsize=(8, 5))
 
plt.plot(
    price_array,
    marker="o"
)
 
# Task 5: Add title and labels
plt.title("House Prices of First 10 Records")
plt.xlabel("Index")
plt.ylabel("Price")
 
plt.tight_layout()
 
# Task 6: Save graph
plt.savefig(
   
         "Graphs/house_prices_line.png"
)
 
plt.show()
plt.close()
 
print("\nScenario 2 completed successfully!")

 #============================================
#Scenario 3: Filtering + Bar Chart + Save 
#============================================
# 1. Filter houses with price > 1,000,000
expensive_houses = df[df["price"] > 1000000]
 
# 2. Count number of houses per bedroom category
bedroom_counts = expensive_houses["bedrooms"].value_counts()
 
# 3. Select top bedroom categories
# Here, top 10 categories are selected
top_bedrooms = bedroom_counts.head(10)
 
# 4. Convert results to NumPy arrays
bedrooms = np.array(top_bedrooms.index)
counts = np.array(top_bedrooms.values)
 
# 5. Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(bedrooms.astype(str), counts)
 
# Labels and title
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Number of Expensive Houses by Bedrooms")
 
# 6. Rotate labels if needed
plt.xticks(rotation=45)
 
plt.tight_layout()
 
# 7. Save graph
plt.savefig("Graphs/expensive_houses_bar.png")
 
"""
Scenario 4: Pie Chart (Bedroom Distribution) + Save

Tasks:
1. Count number of houses by bedrooms
2. Select top 5 bedroom categories
3. Prepare labels and values
4. Plot a pie chart
5. Add percentage labels
6. Save graph: bedroom_distribution.png
"""
# Load & minimal cleaning (bedrooms column needed here)


# Convert to numeric and fill missing values with mode (as per Scenario 1 rules)
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].mode()[0])


# 1. Count number of houses by bedrooms

bedroom_counts = df["bedrooms"].value_counts()


# 2. Select top 5 bedroom categories

top5_bedrooms = bedroom_counts.head(5)

# 3. Prepare labels and values

labels = [f"{int(b)} BHK" for b in top5_bedrooms.index]
values = np.array(top5_bedrooms.values)


# 4 & 5. Plot pie chart with percentage labels

plt.figure(figsize=(7, 7))
plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=plt.cm.Pastel1.colors
)
plt.title("Top 5 Bedroom Categories - House Distribution")
plt.axis("equal")  # keep pie circular

# 6. Save the graph

os.makedirs("graphs", exist_ok=True)
plt.savefig("Graphs/bedroom_distribution.png", bbox_inches="tight")
plt.show()

print("Top 5 bedroom categories:")
print(top5_bedrooms)

#=============================
# Part 1: Feature Creation
# ==============================
 
# Convert price to numeric (safety)
df["price"] = pd.to_numeric(df["price"], errors="coerce")
 
# Create Price Category column
def categorize_price(price):
    if price >= 1000000:
        return "Luxury"
    elif price >= 500000:
        return "Mid Range"
    else:
        return "Affordable"
 
df["price_category"] = df["price"].apply(categorize_price)
 
print("\nPrice Category Counts:")
print(df["price_category"].value_counts())
 
 
# ==============================
# Part 2: NumPy Usage
# ==============================
 
# Convert price column to NumPy array
price_array = df["price"].to_numpy()
 
# Calculate price differences
price_diff = np.diff(price_array)
 
print("\nFirst 10 Price Differences:")
print(price_diff[:10])
 
 
# ==============================
# Part 3: Visualizations
# ==============================
 
# -------- 1. Line Graph --------
price_array = df["price"].dropna().to_numpy()
 
plt.figure(figsize=(10,5))
plt.plot(price_array[:100], marker='o', color="green")
 
plt.title("House Price Trend")
plt.xlabel("Index")
plt.ylabel("Price")
 
plt.tight_layout()
plt.savefig("Graphs/price_trend.png")
plt.show()
 
#---------2. Stacked Bar Chart-----------
# Clean bedrooms column
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["bedrooms"] = df["bedrooms"].round()
 
# Remove unrealistic values (optional but recommended)
df = df[df["bedrooms"] <= 10]
 
# Group by bedrooms and price category
stack_data = df.groupby(["bedrooms", "price_category"]).size().unstack(fill_value=0)
 
# Select top bedroom categories (important fix)
stack_data = stack_data.head(5)
 
# Plot stacked bar chart
stack_data.plot(kind='bar', figsize=(10,6))
 
plt.title("Price Category Distribution by Bedrooms", pad=15)
plt.xlabel("Bedrooms")
plt.ylabel("Count")
 
plt.xticks(rotation=0)
plt.legend(title="Price Category")
 
plt.tight_layout()
plt.savefig("Graphs/price_category_stacked.png")
plt.show()
 
# -------- 3. Histogram --------
plt.figure(figsize=(10,5))
upper_limit = df["price"].quantile(0.95)
filtered_prices = df[df["price"] <= upper_limit]["price"]
plt.hist(filtered_prices, bins=30, color = "gold")
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.ticklabel_format(style='plain', axis='x')
plt.tight_layout()
plt.savefig("Graphs/price_histogram.png")
plt.show()
# ==============================
# Part 5: Insights
# ==============================
 
print("\n========== INSIGHTS ==========")
 
# 1. Bedroom category with most expensive houses
expensive = df[df["price_category"] == "Luxury"]
top_bedroom = expensive["bedrooms"].value_counts().idxmax()
 
print("1. Bedroom category with most expensive houses:", top_bedroom)
 
# 2. Most common price category
common_category = df["price_category"].value_counts().idxmax()
print("2. Most common price category:", common_category)
 
# 3. Distribution pattern
print("3. Price distribution is right-skewed (most houses are in lower price range with few very high values).")