''' Q:Shape Area Calculator (Polymorphism)
A graphics application needs to calculate the area of different shapes. Create classes
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects.'''

class Circle:
    def area(self,radius):
        self.radius=radius
        area=3.14*radius*radius
        print("Circle Area:",area)
class Rectangle:
    def area(self,length,width):
        area=length*width
        print(" Rectangle Area :",area)
        
class Triangle:
    def area(self,side):
        area=3*side
        print(" Trinagle Area :",area)
c=Circle()
r=Rectangle()
t=Triangle()
c.area(3)
r.area(3,4)
t.area(6)

