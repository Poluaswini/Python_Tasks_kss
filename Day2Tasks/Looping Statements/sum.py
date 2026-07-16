# Q:Write a program to find the sum of numbers from 1 to N using a loop.

N=int(input("enter a number:"))
sum=0

for i in range(1,N+1):
    sum=sum+i
print("sum=",sum)