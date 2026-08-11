'''Q:Replace Values Using Filtering
Scenario:
A dataset contains:
[5, 12, 18, 7, 25, 30]
Task:
● Replace all values greater than 15 with 0 using NumPy filtering.'''
import numpy as np
a=[5,12,18,7,25,30]
arr=np.array(a)
arr[arr>15]=0
print(arr)