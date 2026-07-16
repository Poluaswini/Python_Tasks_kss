# Q:Write a program to print the multiplication table of a number using a loop.

number=int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)