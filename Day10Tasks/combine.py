''' Q:Combine Two Sensor Readings
Two sensors record readings during a test.
Scenario:
Sensor1 = [10, 20, 30]
Sensor2 = [40, 50, 60]
Task:
● Store both readings in NumPy arrays.
● Combine them into one array using NumPy concatenation'''

import numpy as np
sensor1 = [10, 20, 30]
sensor2 = [40, 50, 60]
arr1=np.array([sensor1])
arr2=np.array([sensor2])
concatenation=np.concatenate(arr1+arr2)
print(concatenation)