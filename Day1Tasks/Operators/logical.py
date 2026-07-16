# Q:Write a program using logical operators to check age eligibility for voting. 

age=int(input("Enter your age: "))

if age >= 18 and age <= 100:
    print("Eligible for voting")
else:
    print("Not eligible for voting")