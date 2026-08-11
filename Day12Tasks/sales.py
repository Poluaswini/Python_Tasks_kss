'''Q:Random Sales Simulation
Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales.'''
import numpy as np
arr= np.random.randint(100, 501, 10)
print(arr)
average = np.mean(arr)
print(average)