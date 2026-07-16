# Q:Write a program to find the largest of three numbers using if-elif-else.

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

if num1>=num2>=num3:
    print("num1 is largest")
elif num2>=num1>=num3:
    print("num2 is largest")
else:
    print("num3 is largest")