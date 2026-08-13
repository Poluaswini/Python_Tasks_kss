'''Q:Data Analysis Tool (NumPy + Pandas)
Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print results'''
import numpy as np 
import pandas as pd 
arr=np.array([89,60,83,45,99,12])
marks=pd.DataFrame(arr,columns=["marks"])
print(marks)
passed=marks[marks["marks"]>50]
print(passed)
mean=np.mean(arr)
print(mean)
for mark in passed["marks"]:
    print(passed)