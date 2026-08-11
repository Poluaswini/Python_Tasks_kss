'''Q:Random Dataset Normalization + Filtering
Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered value'''
import numpy as np
data = np.random.rand(8)
print("Original data:", data)
normalized = data * 100
filtered = normalized[normalized > 50]
sorted_values = np.sort(filtered)
print("Normalized data:", normalized)
print("Filtered values:", filtered)
print("Sorted values:", sorted_values)