# Q:Write a Python program with a function that returns the largest of three numbers

def largest(a,b,c):
    if a>b>c:
        print("a is largest")
    elif a<b>c:
        print("b is largest")
    else:
        print("c is largest")
largest(10,3,4)