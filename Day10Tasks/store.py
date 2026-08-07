''' Q: Store Sales Comparison
Two stores record daily sales for 3 days.
Scenario:
Store A = [200, 250, 300]
Store B = [180, 270, 310]
Task:
● Store them in NumPy arrays.
● Find the daily difference in sales between the two stores.
● Print the resulting array.'''

import numpy as np
StoreA = [200, 250, 300]
StoreB = [180, 270, 310]
arr1=np.array([StoreA])
arr2=np.array([StoreB])
result=arr1-arr2
print(result)