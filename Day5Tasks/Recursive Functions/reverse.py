# Q:Write a recursive function to reverse a string.
def reverse(s):
    if s=="":
        return ""
    else:
        return reverse(s[1:])+s[0]
string=input("enter String:")
print(reverse(string))
