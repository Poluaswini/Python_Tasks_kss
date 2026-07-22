# Q:Write a function to find the sum of elements in a list using a user-defined function.

def li_sum(li):
    result=0
    for i in li:
        result += i
    return result
li=[1,2,3,4,5]
print("sum:",li_sum(li))