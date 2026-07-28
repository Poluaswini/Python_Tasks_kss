''' Develop a Python program for a small shop to process customer purchases. Store product
names and prices in a dictionary, items added to the cart in a list, product categories in a set,
and product details using tuples. Create functions to display products, add items to the cart, and
calculate the total bill. Use a recursive function to compute the total price of all items in the cart.
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product
name entered by the user does not exist)'''

products = {"Rice":50, "Milk":30, "Soap":40}
cart = []
categories = {"Grocery", "Dairy", "Personal Care"}
product_details = (
    ("Rice", 50, "Grocery"),
    ("Milk", 30, "Dairy"),
    ("Soap", 40, "Personal Care")
)
def recursive_total(cart, index):
    if index == len(cart):
        return 0
    return cart[index] + recursive_total(cart, index + 1)


def display_products():
    print("Avilable Products")
    for name,price in products.items():
        print(name,":" ,price)

def add_item():
    try:
        name=input("enter item name:")
        if name not in products:
            raise NameError
        quantity=int(input("enter quantity:"))
        for i in range(quantity):
            cart.append(products[name])
        print("Added sucessfully")
    except ValueError:
        print("ValueError: Enter numeric quantity only.")

    except NameError:
        print("NameError: Product not found.")
def veiw_total():
    try:
        total = recursive_total(cart, 0)

        average = total / len(cart)      

        print("Total Bill =", total)

    except ZeroDivisionError:
        print("ZeroDivisionError: Cart is empty.")

    except TypeError:
        print("TypeError: Invalid data type in cart.")


        
while True:
    print("\n...Menu...")
    print("1.Display Products")
    print("2.Add items to cart")
    print("3.view total bill")
    print("4.Exit")
    choice=int(input("Enter choie:"))

    if choice==1:
        display_products()
    elif choice==2:
        add_item()
    elif choice==3:
        veiw_total()
    elif choice==4:
        print("Exit")
        break
    else:
        print("Invalid choice")