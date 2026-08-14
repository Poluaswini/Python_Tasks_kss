'''Q:Monthly Sales Analysis
Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales
'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df=pd.DataFrame({
    "sale":sales,
    "month":months
})
print(df)
plt.figure(figsize=(20, 4))
plt.subplot(1,5,1)
plt.plot(df["sale"],df["month"])
plt.title("sales trend")

plt.subplot(1,5,2)
plt.bar(df["sale"],df["month"])
plt.title("month-wise comparison")

plt.subplot(1,5,3)
plt.pie(df["sale"],labels=df["month"],autopct="%1.1f%%")
plt.title("contribution of each month")

plt.subplot(1,5,4)
plt.hist(df["sale"],bins=5)
plt.title("frequency of sales values")

plt.subplot(1,5,5)
plt.scatter(df["sale"],df["month"])
plt.title("month index vs sales")

plt.tight_layout()
plt.show()