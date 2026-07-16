# Q:Write a program to calculate the factorial of a number using a loop.

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial =", factorial)