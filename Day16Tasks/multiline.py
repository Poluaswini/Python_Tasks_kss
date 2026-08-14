'''Q:Multi-Line Graph for Sales Comparison
Scenario:
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]
}
Task:
● Create DataFrame
● Plot two line graphs on same plot
● Add legend'''
import pandas as pd 
import matplotlib.pyplot as plt 
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]
}
d=pd.DataFrame(data)
print(d)
plt.plot(d["Month"],d["Store_A"],label="StoreA")
plt.plot(d["Month"],d["Store_B"],label="StoreB")
plt.legend()
plt.show()