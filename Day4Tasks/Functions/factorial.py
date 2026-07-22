# Q:Write a function that returns the factorial of a number.

# Q: Write a function that returns the factorial of a number.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

result = factorial(5)
print("Factorial:", result)