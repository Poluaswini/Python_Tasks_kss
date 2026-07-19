# Q:Write a program to check whether a string is a palindrome.

a=input("Enter a text:")
b=a[ : : -1]
if a==b:
    print("Palindrome")
else:
    print("Not Palindrome")