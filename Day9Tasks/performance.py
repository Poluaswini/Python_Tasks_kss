''' Q:Performance Tracker (Decorators)
A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function.'''
import time
def track_time(func):
    def wrapper():
        start = time.time()      
        func()                   
        end = time.time()        
        print("Execution Time:", end - start, "seconds")
    return wrapper

@track_time
def display_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)   

display_numbers()