'''Q:Shopping Cart System
Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-excep'''
items=set(['rice','dal','oil'])
print(items)
cost={
    'rice':50,
    'dal':20,
    'oil':100
}
total=0
for item in items:
    try:
        if item in cost:
            total+=cost[item]
        else:
            print("item not there")
    except Exception as e:
        print("No item")
print("Total cost:",total)
        
