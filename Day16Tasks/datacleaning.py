'''Q:Data Cleaning + Visualization
Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

s = pd.Series(data)

print("Original Data:")
print(s)

mean = s.mean()
s = s.fillna(mean)

print("\nCleaned Data:")
print(s)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(s, marker="o")
plt.title("Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Value")

filtered = s[s > mean]

plt.subplot(1, 2, 2)
plt.bar(filtered.index, filtered.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Value")

plt.tight_layout()
plt.show()