''' Q:2. Rectangle Area Calculator (Constructor)
A geometry application needs to calculate the area of rectangles. Create a Rectangle
class that uses a constructor to initialize length and width. Add a method to calculate
and display the area.'''
class Rectangle:  
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        print("Length:",self.length)
        print("Width:",self.width)
        area=self.length*self.width
        print("Area:",area)
r1=Rectangle(10,8)
r1.area()

