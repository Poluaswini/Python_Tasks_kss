# Q:Write a program to check whether a given number is an Armstrong number or not.

num=int(input("Enter a number:"))
original=num
result=0
while num>0:
    digit=num % 10
    result+=digit ** 3
    num //= 10
if original==result:
    print("Armstrong number")
else:
    print("Not Armstrong number")

