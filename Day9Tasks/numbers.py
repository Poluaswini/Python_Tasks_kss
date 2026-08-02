''' Q:Random Number Generator (Generators)
A program is needed to generate numbers for testing purposes. Create a generator
function that produces numbers from 1 to N and prints them one by one when iterated.
'''

def num_gen(n):
    for i in range(1,n+1):
        yield i 
N=int(input("enter Number:"))
gen=num_gen(N)
for num in gen:
    print(num)