'''Q:Student Score Processor
Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file'''
import math
name=('aswini','sathu','buddi')
marks=(90,91,90)
student=dict(zip(name,marks))
print(student)
count=0
for name, mark in student.items():
    if mark > 50:
        count += 1
print(count)
average = math.fsum(marks) / len(marks)
print(average)

file=open("text.txt","w")
file.write("student details \n")
file.write(str(student))
file.write("Marks Greater than 50:\n")
file.write(str(count))
file.write("average"+ str(average))