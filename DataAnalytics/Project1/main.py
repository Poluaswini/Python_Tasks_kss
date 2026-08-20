import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

#Scenario 1: Basic Data Loading & Cleaning
df=pd.read_csv("railway_gauges.csv")
print(df.head())
print(df.isnull().sum())  # for missing values
df=df.fillna(0)  # replace with 0
print(df.head())
gauge_columns = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]
df[gauge_columns] = df[gauge_columns].apply(pd.to_numeric)
print(df.dtypes)

#Scenario 2: Simple Visualization
data=df[["Year","Total"]]
print(df.head())
plt.plot(data["Year"],data["Total"])
plt.title(" Total tracks over years")
plt.xlabel("Years")
plt.ylabel("Total tracks")
plt.xticks(rotation=60)
plt.savefig("graphs/total_railway_growth.png")

#Scenario 3: Filtering + Bar Chart
# Filter dataset for years after 2000
df["Start Year"] = df["Year"].str[:4].astype(int)
recent = df[df["Start Year"] > 2000]
print(recent)
gauge_data = recent[["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]]
print(gauge_data)
gauge_data.plot(
    x="Year",
    y=["Broad Gauge", "Metre Gauge", "Narrow Gauge"],
    kind="bar",
    figsize=(12, 6)
)
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(rotation=45)
plt.savefig("graphs/gauge_comparison_after_2000.png")


#Scenario 4: Feature Engineering + Pie Chart
#Calculate total sum of each gauge
gauge_totals = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print("Total of each gauge:")
print(gauge_totals)

#gauge_totals is already a Pandas Series

#Create pie chart with percentage labels
plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct="%1.1f%%"
)
plt.title("Railway Gauge Contribution")
plt.savefig("graphs/gauge_contribution.png")

#Find gauge with highest contribution
highest_gauge = gauge_totals.idxmax()
print("Gauge with the highest contribution:", highest_gauge)
print("Highest contribution:", gauge_totals[highest_gauge])

#Scenario 5: Advanced Analysis + Multiple Graphs
#Create percentage columns
df["% Broad Gauge"] = (
    df["Broad Gauge"] / df["Total"]
) * 100

df["% Metre Gauge"] = (
    df["Metre Gauge"] / df["Total"]
) * 100

df["% Narrow Gauge"] = (
    df["Narrow Gauge"] / df["Total"]
) * 100

print("\nGauge Percentage:")
print(df[["Year","% Broad Gauge","% Metre Gauge","% Narrow Gauge"]])

#Calculate yearly growth using np.diff()
growth = np.diff(df["Total"])
df["Yearly Growth"] = np.nan
df.loc[df.index[1:], "Yearly Growth"] = growth
print("\nYearly Total Growth:")
print( df[["Year","Total","Yearly Growth"]])

#Find year with highest growth
highest_growth_index = df["Yearly Growth"].idxmax()
print("\nHighest Growth Year:")
print(df.loc[highest_growth_index, "Year"])
print("Highest Growth:")
print(df.loc[highest_growth_index, "Yearly Growth"])

#Line graph for all gauges
plt.figure(figsize=(12, 6))
plt.plot(
    df["Year"],
    df["Broad Gauge"],
    label="Broad Gauge"
)

plt.plot(
    df["Year"],
    df["Metre Gauge"],
    label="Metre Gauge"
)

plt.plot(
    df["Year"],
    df["Narrow Gauge"],
    label="Narrow Gauge"
)

plt.title("Railway Gauge Trends")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/all_gauge_trends.png")

#Stacked bar chart
plt.figure(figsize=(12, 6))
plt.bar(
    df["Year"],
    df["Broad Gauge"],
    label="Broad Gauge"
)

plt.bar(
    df["Year"],
    df["Metre Gauge"],
    bottom=df["Broad Gauge"],
    label="Metre Gauge"
)

plt.bar(
    df["Year"],
    df["Narrow Gauge"],
    bottom=df["Broad Gauge"] + df["Metre Gauge"],
    label="Narrow Gauge"
)

plt.title("Railway Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/gauge_composition.png")

#Identify decline in each gauge

gauges = [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge"
]
print("\nGauge Decline Analysis:")
for gauge in gauges:
    changes = np.diff(df[gauge])
    decline_indices = np.where(changes < 0)[0]
    print("\n" + gauge)
    if len(decline_indices) == 0:
        print("No decline found.")
    else:
        print("Decline occurred in:")
        for index in decline_indices:
            print(
                df.iloc[index + 1]["Year"]
            )

#Compare percentage contribution
broad_start = df["% Broad Gauge"].iloc[0]
broad_end = df["% Broad Gauge"].iloc[-1]

metre_start = df["% Metre Gauge"].iloc[0]
metre_end = df["% Metre Gauge"].iloc[-1]

narrow_start = df["% Narrow Gauge"].iloc[0]
narrow_end = df["% Narrow Gauge"].iloc[-1]

print("\nPercentage Comparison:")

print(
    "Broad Gauge:",
    round(broad_start, 2),
    "→",
    round(broad_end, 2)
)

print(
    "Metre Gauge:",
    round(metre_start, 2),
    "→",
    round(metre_end, 2)
)

print(
    "Narrow Gauge:",
    round(narrow_start, 2),
    "→",
    round(narrow_end, 2)
)
#Final Conclusion
print("FINAL CONCLUSION")

if (
    broad_end > broad_start
    and metre_end < metre_start
    and narrow_end < narrow_start
):

    print(
        "Yes, the railway system is shifting "
        "towards a single dominant gauge."
    )

    print(
        "Broad Gauge has increased its percentage "
        "contribution while Metre Gauge and Narrow "
        "Gauge have decreased."
    )

else:

    print(
        "The railway system is not clearly shifting "
        "towards a single dominant gauge based on "
        "the percentage contribution."
    )