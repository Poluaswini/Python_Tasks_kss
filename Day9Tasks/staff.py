'''Q:University Staff Management (Hierarchical Inheritance)
A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information.'''
class Staff:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Professor(Staff):
    def display(self):
        print("Professor Details")
        print("Name:", self.name)
        print("ID :", self.id)
class LabAssistant(Staff):
    def display(self):
        print("LabAssistant Details")
        print("Name:", self.name)
        print("ID :", self.id)
class Administrator(Staff):
    def display(self):
        print("Admimistrator Details")
        print("Name:", self.name)
        print("ID :", self.id)
p=Professor("xyz","101")
l=LabAssistant("abc","102")
a=Administrator("gfh","103")
p.display()
l.display()
a.display()
