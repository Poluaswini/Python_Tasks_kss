# Q:Write a program to count the frequency of each character in a string.

a="hello world"
frequency={}
for i in a:
    if i in frequency:
       frequency[i]+=1
    else:
       frequency[i]=1
print(frequency)