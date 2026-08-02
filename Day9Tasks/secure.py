''' Q:Secure Login System (Decorators)
A web application wants to ensure that users are authenticated before accessing
sensitive functions. Create a decorator that checks whether the user is logged in before
allowing access to a function.'''

def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func(is_logged_in)
        else:
            print("Access Denied! Please log in first.")
    return wrapper

@login_required
def view_profile(is_logged_in):
    print("Welcome! Accessing your profile.")
status = input("Are you logged in? (yes/no): ").lower()
if status == "yes":
    view_profile(True)
else:
    view_profile(False)