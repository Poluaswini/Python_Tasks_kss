'''Q:Copy vs View Behavior in Data Processing
Scenario:
A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference.'''
import numpy as np
copy_data = data.copy()
data[0] = 100
print("Original array:", data)
print("Copy:", copy_data)
data = np.array([10, 20, 30, 40])
view_data = data.view()
data[0] = 100
print("\nOriginal array:", data)
print("View:", view_data)