''' Q:1. Student Information System (Class & Object)
A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details.'''

class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def display(self):
        print("name:",self.name)
        print("roll:",self.roll)
        print("marks:",self.marks)
    
s1=Student("Aswini",23,90)
s2=Student("Satvika",24,89)
s3=Student("Aswitha",25,90)
s1.display()
s2.display()
s3.display()

