'''Q:Pie Chart with Conditional Data
Scenario:
scores = np.array([40, 60, 80, 30, 90])
Task:
● Categorize into:
○ Pass (>50)
○ Fail (<=50)
● Count using NumPy/Pandas
● Plot pie chart for Pass vs Fail'''
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
scores = np.array([40, 60, 80, 30, 90])
passed=np.array(scores[scores>50])
fail=np.array(scores[scores<=50])
count=pd.Series({
    "pass":len(passed),
    "fail":len(fail)
})
print(count)
plt.pie(count,labels=count.index,autopct="%1.1f%%")
plt.show()
