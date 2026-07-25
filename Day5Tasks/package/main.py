""" A company wants to organize its Python code using packages.
Create a package named utilities that contains two modules:
● math_operations.py (functions for addition and multiplication)
● string_operations.py (functions to convert string to uppercase and count
characters)
Write a Python program that imports the package and uses functions from both modules"""

from utilities import math_operations
from utilities import string_operations

a=int(input("enter a number:"))
b=int(input("enter b number:"))
s=input("enter a text:")
print("Addition:", math_operations.addition(a, b))
print("Multiplication:", math_operations.multiplication(a, b))
print("Uppercase:", string_operations.uppercase(s))
print("Number of characters:", string_operations.count(s))

