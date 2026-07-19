# Q:Write a program to find the student with the highest marks from a dictionary.
a={
    "aswini":99,
    "satvika":98,
    "aswitha":97
}
highest = max(a, key=a.get)
print(highest)