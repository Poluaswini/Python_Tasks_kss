'''Q:Product Sales Bar Chart
Scenario:
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
Task:
● Create DataFrame
● Plot bar chart
● Add labels and title
'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
d=pd.DataFrame(products,sales)
print(d)
plt.bar(products,sales)
plt.xlabel("products")
plt.ylabel("sales")
plt.title("Product Sales")
plt.show()