class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        area = self.height*self.width
        print(f"Area of reactangle: {area}")
    def perimeter(self):
        peri = 2*(self.height+self.width)
        print(f"Perimeter of recatngle: {peri}")


rectangle = Rectangle(height=10,width=20)
rectangle.area()
rectangle.perimeter()