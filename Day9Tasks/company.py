''' Q: 3. Employee Salary System (Simple Inheritance)
A company has two types of employees: Employee and Manager. Create a base class
Employee containing name and salary. Create a derived class Manager that inherits
from Employee and displays the employee details.'''

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def display_details(self):
        print("Employee Name :", self.name)
        print("Employee Salary :", self.salary)

a=Manager("Aswini",30000)
a.display_details()