# Q:Write a program to check whether a number is a Perfect number.

num=int(input("Enter a number: "))
total=0
for i in range(1, num):
    if num%i==0:
        total+=i

if total==num:
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")