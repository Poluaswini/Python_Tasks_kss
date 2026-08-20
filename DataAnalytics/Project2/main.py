import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# LOAD DATASET
df = pd.read_csv("ign.csv")
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nShape of dataset:")
print(df.shape)
# SCENARIO 1: DATA LOADING & PREPROCESSING
# Remove unnecessary column if it exists
if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

# Check missing values
print("\nMissing values:")
print(df[["score", "genre", "platform"]].isnull().sum())

# Fill score with mean
df["score"] = df["score"].fillna(df["score"].mean())

# Fill genre with mode
df["genre"] = df["genre"].fillna(df["genre"].mode()[0])

# Convert data types
df["score"] = df["score"].astype(float)
df["release_year"] = df["release_year"].astype(int)
df["release_month"] = df["release_month"].astype(int)
df["release_day"] = df["release_day"].astype(int)

print("\nData types:")
print(df.dtypes)

print("\nMissing values after handling:")
print(df[["score", "genre", "platform"]].isnull().sum())


# SCENARIO 2: LINE GRAPH

# Group by release year and calculate average score
yearly_score = df.groupby("release_year")["score"].mean()

print("\nAverage score per year:")
print(yearly_score)

# Convert to NumPy arrays
years = np.array(yearly_score.index)
average_scores = np.array(yearly_score.values)

# Plot line graph
plt.figure(figsize=(10, 5))

plt.plot(years, average_scores, marker="o")

plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")

plt.grid(True)
plt.tight_layout()
plt.savefig("Graph/avg_score_trend.png")

# SCENARIO 3: FILTERING + BAR CHART

# Filter games where score > 7
high_rated = df[df["score"] > 7]

# Count high-rated games per platform
platform_counts = high_rated["platform"].value_counts()

# Select top 10 platforms
top_10_platforms = platform_counts.head(10)

print("\nTop 10 Platforms:")
print(top_10_platforms)

# Convert to NumPy arrays
platforms = np.array(top_10_platforms.index)
game_counts = np.array(top_10_platforms.values)

# Plot bar chart
plt.figure(figsize=(10, 6))

plt.bar(platforms, game_counts)

plt.title("Top 10 Platforms with High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Count of Games")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Graph/top_platforms_bar.png")

# SCENARIO 4: AGGREGATION + PIE CHART

# Count games per genre
genre_counts = df["genre"].value_counts()

# Select top 5 genres
top_5_genres = genre_counts.head(5)

print("\nTop 5 Genres:")
print(top_5_genres)

labels = np.array(top_5_genres.index)
values = np.array(top_5_genres.values)

# Plot pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)
plt.title("Top 5 Game Genre Distribution")
plt.savefig("Graph/genre_distribution.png")

