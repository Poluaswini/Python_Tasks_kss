'''Q:Random Number Analyzer
Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates'''
import random
number=[]
for i in range(10):
    number.append(random.randint(1,100))
print(number)
a=list(number)
print(a)
even=0
odd=0
for n in number:
    if n%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)
