'''Q:Accessing Matrix Data
A teacher stores marks of students in two subjects:
[[78, 85],
[90, 88],
[67, 72]]
Task:
● Convert it to a NumPy array.
● Access the second student's second subject mark.'''
import numpy as np
marks = [
    [78, 85],
    [90, 88],
    [67, 72]
]
arr = np.array(marks)
print("Mark:", arr[1, 1])