# Q:Write a program to check whether a given number is a Strong number.
import math
num=int(input("Enter a number: "))
original = num
total = 0

while num>0:
    digit=num%10
    total +=math.factorial(digit)
    num //= 10

if total==original:
    print(original, "is a Strong number")
else:
    print(original, "is not a Strong number")