import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# ================================================================
# SCENARIO 1: DATA LOADING & PREPROCESSING
# ================================================================

# Load dataset using Pandas
data = pd.read_csv(
    "ign.csv"
)

# Create Graph folder if it does not exist
os.makedirs("Graph", exist_ok=True)


# First 5 rows
print("Displaying the first 5 rows of data:")
print(data.head())
print("------------------------------------------------------------------------------")


# Last 5 rows
print("Displaying the last 5 rows of data:")
print(data.tail())
print("------------------------------------------------------------------------------")


# Shape of dataset
print("The shape of the dataset is:")
print(data.shape)
print("------------------------------------------------------------------------------")


# Remove unnecessary column
data.drop(
    columns=["Unnamed: 0"],
    inplace=True,
    errors="ignore"
)

print("Removed the column Unnamed!!")
print("------------------------------------------------------------------------------")


# Check missing values
missing_values = data[
    ["score", "genre", "platform"]
].isnull().sum()

print("Total missing values before handling:")
print(missing_values)
print("------------------------------------------------------------------------------")


# Fill score with mean
average_score = data["score"].mean()

data["score"] = data["score"].fillna(
    average_score
)


# Fill genre with mode
if not data["genre"].mode().empty:

    mode_val_genre = data["genre"].mode()[0]

    data["genre"] = data["genre"].fillna(
        mode_val_genre
    )


print("Replaced missing values correctly!!")
print("------------------------------------------------------------------------------")


# Check missing values after handling
missing_values_after = data[
    ["score", "genre", "platform"]
].isnull().sum()

print("Total missing values AFTER handling:")
print(missing_values_after)
print("------------------------------------------------------------------------------")


# Change data types
data = data.astype({
    "score": "float64",
    "release_year": "int32",
    "release_month": "int32",
    "release_day": "int32"
})

print("Changed the type of columns into their respective types")
print("------------------------------------------------------------------------------")


# ================================================================
# SCENARIO 2: LINE GRAPH
# ================================================================

# Group by release year
grouped_year = data.groupby(
    "release_year"
)["score"].mean()

print("The average score for respective years is:")
print(grouped_year)
print("------------------------------------------------------------------------------")


# Convert Pandas results into NumPy arrays
years = grouped_year.index.to_numpy()
avg_scores = grouped_year.values


# Plot line graph
plt.figure(figsize=(10, 5))

plt.plot(
    years,
    avg_scores,
    marker="o"
)

plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "Graph/avg_score_trend.png"
)

plt.show()

print("Scenario 2 completed!")
print("------------------------------------------------------------------------------")


# ================================================================
# SCENARIO 3: FILTERING + BAR CHART
# ================================================================

# Filter games where score > 7
filtered_data = data[
    data["score"] > 7
]

print("Number of high-rated games:")
print(len(filtered_data))
print("------------------------------------------------------------------------------")


# Count high-rated games per platform
top_rated_games = filtered_data.groupby(
    "platform"
)["title"].count()

print("High-rated games per platform:")
print(top_rated_games)
print("------------------------------------------------------------------------------")


# Select top 10 platforms
top_10 = top_rated_games.sort_values(
    ascending=False
).head(10)

print("Top 10 platforms:")
print(top_10)
print("------------------------------------------------------------------------------")


# Convert to NumPy arrays
platforms = top_10.index.to_numpy()
counts = top_10.values


print("Platforms:")
print(platforms)

print("Counts:")
print(counts)
print("------------------------------------------------------------------------------")


# Plot bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    platforms,
    counts
)

plt.title(
    "Top 10 Platforms by High-Rated Games"
)

plt.xlabel("Platform")
plt.ylabel("Number of Games")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "Graph/top_platforms_bar.png"
)

plt.show()

print("Scenario 3 completed!")
print("------------------------------------------------------------------------------")


# ================================================================
# SCENARIO 4: AGGREGATION + PIE CHART
# ================================================================

# Count games per genre
genre_counts = data[
    "genre"
].value_counts()

print("The number of games per genre:")
print(genre_counts)
print("------------------------------------------------------------------------------")


# Select top 5 genres
top_5 = genre_counts.head(5)

print("Top 5 genres:")
print(top_5)
print("------------------------------------------------------------------------------")


# Prepare labels and values
genres = top_5.index.to_numpy()
counts = top_5.values


# Plot pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    counts,
    labels=genres,
    autopct="%1.1f%%"
)

plt.title(
    "Top 5 Game Genre Distribution"
)

plt.tight_layout()

plt.savefig(
    "Graph/genre_distribution.png"
)

plt.show()

print("Scenario 4 completed!")
print("------------------------------------------------------------------------------")


# ================================================================
# SCENARIO 5: ADVANCED ANALYSIS + MULTIPLE GRAPHS
# ================================================================


# ================================================================
# PART 1: FEATURE ENGINEERING
# ================================================================

# Create score_category
data["score_category"] = np.where(
    data["score"] >= 9,
    "Excellent",
    np.where(
        data["score"] >= 7,
        "Good",
        "Average"
    )
)

print("Score category column created!")

print(
    data[
        ["score", "score_category"]
    ].head()
)

print("------------------------------------------------------------------------------")


# Convert editors_choice
# Y -> 1
# N -> 0

data["editors_choice"] = data[
    "editors_choice"
].map({
    "Y": 1,
    "N": 0
})

print("Converted editors_choice to numeric!")

print(
    data[
        ["editors_choice"]
    ].head()
)

print("------------------------------------------------------------------------------")


# ================================================================
# PART 2: NUMPY ANALYSIS
# ================================================================

# Calculate average score per year
yearly_avg = data.groupby(
    "release_year"
)["score"].mean()


# Convert to NumPy arrays
years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values


# Calculate yearly score growth using np.diff()
score_growth = np.diff(
    avg_scores
)

print("Yearly score growth:")
print(score_growth)

print("------------------------------------------------------------------------------")


# ================================================================
# PART 3: VISUALIZATIONS
# ================================================================


# ------------------------------------------------
# 1. LINE GRAPH
# ------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    years,
    avg_scores,
    marker="o"
)

plt.title(
    "Average Score Trend Over Years"
)

plt.xlabel(
    "Release Year"
)

plt.ylabel(
    "Average Score"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Graph/score_trend.png"
)

plt.show()

print("Score trend graph saved!")
print("------------------------------------------------------------------------------")


# ------------------------------------------------
# 2. STACKED BAR CHART
# ------------------------------------------------

# Create pivot table
category_counts = data.pivot_table(
    index="release_year",
    columns="score_category",
    aggfunc="size",
    fill_value=0
)


# Make sure categories appear in desired order
category_order = [
    "Average",
    "Good",
    "Excellent"
]

category_counts = category_counts.reindex(
    columns=category_order,
    fill_value=0
)


# Plot stacked bar chart
category_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

plt.title(
    "Score Category Distribution per Year"
)

plt.xlabel(
    "Release Year"
)

plt.ylabel(
    "Number of Games"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "Graph/score_category_stacked.png"
)

plt.show()

print("Stacked bar chart saved!")
print("------------------------------------------------------------------------------")


# ------------------------------------------------
# 3. HISTOGRAM
# ------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    data["score"],
    bins=20
)

plt.title(
    "Score Distribution"
)

plt.xlabel(
    "Score"
)

plt.ylabel(
    "Frequency"
)

plt.tight_layout()

plt.savefig(
    "Graph/score_distribution.png"
)

plt.show()

print("Score distribution graph saved!")
print("------------------------------------------------------------------------------")


# ================================================================
# PART 5: INSIGHTS
# ================================================================


# ------------------------------------------------
# 1. YEAR WITH HIGHEST AVERAGE SCORE
# ------------------------------------------------

max_year = yearly_avg.idxmax()
max_score = yearly_avg.max()

print(
    f"Year with highest average score: "
    f"{max_year} ({max_score:.2f})"
)

print("------------------------------------------------------------------------------")


# ------------------------------------------------
# 2. CHECK OVERALL TREND
# ------------------------------------------------

average_growth = score_growth.mean()

print(
    f"Average yearly score growth: "
    f"{average_growth:.4f}"
)

if average_growth > 0:

    print(
        "Overall trend: Scores are increasing over time"
    )

elif average_growth < 0:

    print(
        "Overall trend: Scores are decreasing over time"
    )

else:

    print(
        "Overall trend: Scores are remaining stable"
    )

print("------------------------------------------------------------------------------")


# ------------------------------------------------
# 3. EDITORS' CHOICE VS SCORE
# ------------------------------------------------

editors_avg = data.groupby(
    "editors_choice"
)["score"].mean()

print(
    "Average score based on editors_choice:"
)

print(editors_avg)

print("------------------------------------------------------------------------------")


# Safely compare Editors' Choice and non-Editors' Choice
editors_choice_score = editors_avg.get(1, 0)
non_editors_choice_score = editors_avg.get(0, 0)


if editors_choice_score > non_editors_choice_score:

    print(
        "Editors' Choice games generally have higher scores"
    )

elif editors_choice_score < non_editors_choice_score:

    print(
        "Non-Editors' Choice games generally have higher scores"
    )

else:

    print(
        "Editors' Choice and non-Editors' Choice games "
        "have the same average score"
    )

print("------------------------------------------------------------------------------")


# ================================================================
# FINAL OUTPUT
# ================================================================

print("\nAll scenarios completed successfully!")

print("\nGraphs saved inside the Graph folder:")

print("1. avg_score_trend.png")
print("2. top_platforms_bar.png")
print("3. genre_distribution.png")
print("4. score_trend.png")
print("5. score_category_stacked.png")
print("6. score_distribution.png")