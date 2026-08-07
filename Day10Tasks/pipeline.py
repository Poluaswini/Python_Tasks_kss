''' Q: Data Processing Pipeline
A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each part'''
import numpy as np
arr=np.array([12,7,25,3,18,10])
a=np.sort(arr)
b=np.split(a,2)
s1=np.sum(b[0])
s2=np.sum(b[1])
print("sort:",a)
print("split:",b)
print("Sum1:",s1)
print("Sum2:",s2)