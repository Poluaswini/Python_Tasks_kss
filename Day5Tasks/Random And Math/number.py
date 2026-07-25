""" Write a Python program that generates 20 random numbers between 1 and 200 using
the random module and store them in a list.
Then using the math module, compute and display:
● Maximum value
● Minimum value
● Square root of the maximum number
● Logarithm of the minimum number"""

import random
import math

num=[]
for i in range(20):
    num.append(random.randint(1,200))
print(num)
maximum=max(num)
minimum=min(num)
print(maximum)
print(minimum)
print(math.sqrt(maximum))
print(math.log(minimum))
