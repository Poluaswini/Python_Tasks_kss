'''Q:Product Rating Normalization
Ratings from different users:
ratings = np.array([2, 3, 4, 5, 1])
Task:
● Normalize ratings to a range 0 to 1 using:
normalized = (value - min) / (max - min)'''
import numpy as np
ratings = np.array([2, 3, 4, 5, 1])
min_value = np.min(ratings)
max_value = np.max(ratings)
normalized = (ratings - min_value) / (max_value - min_value)
print("Original ratings:", ratings)
print("Normalized ratings:", normalized)