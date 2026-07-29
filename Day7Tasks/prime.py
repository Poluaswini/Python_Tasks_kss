# Q:Write a program to check whether a number is Prime.

num=int(input("Enter a number: "))
count=0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count==2:
    print("Factors = 1,", num)
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")