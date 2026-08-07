'''Q:9. Multi-Department Data Aggregation
A company collects employee counts from two branches.
Branch A:
[[10, 20],
[30, 40]]
Branch B:
[[5, 15],
[25, 35]]
Scenario:
● Combine the two matrices.
● Calculate the total employees across all departments.
● Print the combined matrix and total.'''
import numpy as np
BranchA=[[10, 20],[30, 40]]
BranchB=[[5, 15],[25, 35]]
arr1=np.array(BranchA)
arr2=np.array(BranchB)
a=np.add(arr1,arr2)
print(a)
print(np.sum(a))