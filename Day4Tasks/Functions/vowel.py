# Q: Write a function that takes a string as input and returns the number of vowels.

a=input("Enter a string: ")

def vowel(a):
    result=0
    for i in a:
        if i.lower() in "aeiou":
            result += 1
    return result

print("Number of vowels:", vowel(a))