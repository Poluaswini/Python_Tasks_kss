'''Q:Employee Salary Insights
Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({
    "Salary": salaries,
    "Department": departments
})

print(df)

plt.figure(figsize=(20, 4))

plt.subplot(1, 5, 1)
plt.plot(df.index, df["Salary"], marker="o")
plt.title("Salary Trend")
plt.xlabel("Index")
plt.ylabel("Salary")

dept_salary = df.groupby("Department")["Salary"].sum()

plt.subplot(1, 5, 2)
plt.bar(dept_salary.index, dept_salary.values)
plt.title("Department-wise Salary")
plt.xlabel("Department")
plt.ylabel("Total Salary")

dept_count = df["Department"].value_counts()

plt.subplot(1, 5, 3)
plt.pie(
    dept_count,
    labels=dept_count.index,
    autopct="%1.1f%%"
)
plt.title("Department Distribution")

plt.subplot(1, 5, 4)
plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.subplot(1, 5, 5)
plt.scatter(df.index, df["Salary"])
plt.title("Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()