from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area():
        pass
    
    @abstractmethod
    def circumfrence():
        pass

class circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi*self.radius*self.radius
        print(area)
    def circumfrence(self):
        circum = 2*math.pi*self.radius
        print(circum)


"""Alternate Method"""
class circle1(shape):

    def area(self,radius):
        area = math.pi*radius*radius
        print(area)
    def circumfrence(self,radius):
        circum = 2*math.pi*radius
        print(circum)


c1 = circle(radius=2)
c1.area()
c1.circumfrence()

c2 = circle1()
c2.area(radius=2)
c2.circumfrence(radius=2)

class square(shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side*self.side
        print(area)
    def circumfrence(self):
        circum = 4*self.side
        print(circum)


"""Alternate Method"""
class square1(shape):

    def area(self,side):
        area = side*side
        print(area)
    def circumfrence(self,side):
        circum = 4*side
        print(circum)

s1 = square(side=2)
s1.area()
s1.circumfrence()

s2 = square1()
s2.area(side=2)
s2.circumfrence(side=2)