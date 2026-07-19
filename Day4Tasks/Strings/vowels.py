# Q:Write a program to count the number of vowels in a string.
a=input("enter a string:")
count=0
for i in a:
    if i.lower() in 'aeiou':
        count+=1
print("vowels:" , count)