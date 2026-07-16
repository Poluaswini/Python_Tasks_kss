# Q:Write a program that searches for a number in a list and breaks the loop when found.

list=[10,20,30,40]
search=int(input("enter a number:"))

for i in list:
    if i==search:
        break
    print(i)