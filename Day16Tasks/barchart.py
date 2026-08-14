'''Q:Student Marks Bar Chart
Scenario:
Marks of students:
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
Task:
● Create a DataFrame
● Plot a bar graph
● Show student names on X-axis'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
data=pd.DataFrame(names,marks)
print(data)
plt.bar(names,marks)
plt.xlabel(names)
plt.show()