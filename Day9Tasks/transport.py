''' Q:Vehicle Management System (Inheritance)
A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details.'''

class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Car(Vehicle):
    def display(self):
        print("Car Details")
        print("Brand :", self.brand)
        print("Speed :", self.speed, "km/h")
class Bike(Vehicle):
    def display(self):
        print("Car Details")
        print("Brand :", self.brand)
        print("Speed :", self.speed, "km/h")
c=Car("BMW","101")
b=Bike("Honda","45")
c.display()
b.display()
