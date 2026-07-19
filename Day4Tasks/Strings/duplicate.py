# Q:Write a program to remove duplicate characters from a string.
a=input("enter text:")
duplicate=""
for i in a:
    if i not in duplicate:
        duplicate+=i
print(duplicate)