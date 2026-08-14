'''Q:Temperature Monitoring System
Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

plt.figure(figsize=(20, 4))

plt.subplot(1, 5, 1)
plt.plot(df["Day"], df["Temperature"], marker="o")
plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.subplot(1, 5, 2)
plt.bar(df["Day"], df["Temperature"])
plt.title("Day-wise Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")

high = np.sum(temps > 30)
low = np.sum(temps <= 30)

plt.subplot(1, 5, 3)
plt.pie(
    [high, low],
    labels=["High (>30)", "Low (<=30)"],
    autopct="%1.1f%%"
)
plt.title("High vs Low Temperature")

plt.subplot(1, 5, 4)
plt.hist(df["Temperature"], bins=5)
plt.title("Temperature Frequency")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

plt.subplot(1, 5, 5)
plt.scatter(df.index, df["Temperature"])
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")

plt.tight_layout()
plt.show()