'''Q:Student Performance Dashboard
Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
df=pd.DataFrame({
    "mark":marks,
    "student":students
})
print(df)
plt.figure(figsize=(20, 4))
plt.subplot(1,5,1)
plt.plot(df["mark"],df["student"])
plt.title("Trend of marks")

plt.subplot(1,5,2)
plt.bar(df["mark"],df["student"])
plt.title("Student Vs Marks")

passed=np.sum(marks>50)
failed=np.sum(marks<=50)
plt.subplot(1,5,3)
plt.pie([passed,failed],labels=["Pass","Fail"],autopct="%1.1f%%")
plt.title("Pass (>50) vs Fail")

plt.subplot(1,5,4)
plt.hist(df["mark"],bins=5)
plt.title("distribution of marks")

plt.subplot(1,5,5)
plt.scatter(df.index,df["mark"])
plt.title("index vs marks")
plt.show()