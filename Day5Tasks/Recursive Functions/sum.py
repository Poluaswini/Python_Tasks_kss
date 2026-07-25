# Q:Write a recursive function to calculate the sum of digits of a number.Example: Input = 123 → Output = 6

def sum(n):
    if n==0 :
        return 0
    else:
        return (n % 10) + sum(n // 10) 
print(sum(234))