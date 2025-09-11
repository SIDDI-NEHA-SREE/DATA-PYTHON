'''Create an abstract class Shape that defines:
 
An abstract method area() (no implementation).
Create two child classes that inherit from Shape:
Rectangle → has attributes length, breadth, and implements area().
Circle → has attribute radius, and implements area().
Task:
Define the abstract class Shape using the abc module.
Implement Rectangle and Circle classes by providing their own version of area().
Create one object of Rectangle and one of Circle, then display their areas.
 
from abc import ABC, abstractmethod
 
# Abstract class
class Shape(ABC):
 
    @abstractmethod           # Abstract method
    def area(self):
        pass   '''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return f"Area of rectangele: {self.l*self.b}squnits"
class circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return f"Area of circle: {3.14*self.r**2}squnits"
    

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
s = rectangle(l, b)
print(s.area())
r = int(input("Enter radius: "))
d = circle(r)
print(d.area())