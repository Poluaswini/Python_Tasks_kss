'''Q:Random Data & Filtering
Generate random numbers:
nums = np.random.randint(1, 100, 10)
Task:
● Filter values that are divisible by 5
● Return sorted result'''
import numpy as np
nums = np.random.randint(1, 100, 10)
print("Original numbers:", nums)
filtered = nums[nums % 5 == 0]
sorted_result = np.sort(filtered)
print("Sorted values divisible by 5:", sorted_result)