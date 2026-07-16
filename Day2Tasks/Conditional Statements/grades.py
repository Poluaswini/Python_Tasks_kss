# Q:Write a program to assign grades based on marks (for example: A, B, C, Fail).

marks=int(input("enter marks:"))

if marks>=85:
    print("A")
elif marks >=75:
    print("B")
elif marks >=65:
    print("C")
else:
    print("Fail")