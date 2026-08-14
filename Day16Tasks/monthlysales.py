'''Q:Monthly Sales Line Graph
Scenario:
A shop records monthly sales:
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]
Task:
● Convert data into a Pandas DataFrame
● Plot a line graph
● Label X-axis as months and Y-axis as sales'''
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]
data=pd.DataFrame(sales,months)
print(data)
plt.plot(sales,months)
plt.xlabel("Months")
plt.ylabel("sales")
plt.show()