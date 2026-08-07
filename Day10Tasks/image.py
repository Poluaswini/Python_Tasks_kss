'''Q:Matrix Transformation in Image Processing
An image processing system stores pixel intensity values in a matrix.
Scenario:
[[1, 2],
[3, 4]]
Task:
● Create a NumPy array for this matrix.
● Find its transpose.
● Print both matrices.'''

import numpy as np 
a=[[1,2],[3,4]]
arr=np.array(a)
print(arr)
print(np.transpose(arr))