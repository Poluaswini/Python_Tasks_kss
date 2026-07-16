# Q:Write a program to check whether a number is positive, negative, or zero.

num=int(input("enter a number:"))

if num>0:
    print( num , "number is positive")
elif num==0:
    print("given number is zero")
else:
    print("given number is negative")