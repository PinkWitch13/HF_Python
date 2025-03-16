"""1. Create Rectangle and Square classes with 
    a method called calculate_perimeter that 
    calculates the perimeter of the shapes
    they represent. Create Rectangle and 
    Square objects and call the method on both of them"""

class Rectangle():
    def __init__ (self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter (self):
        return (self.width * 2) + (self.len * 2)

class Square (Rectangle):
    pass

rectangle_1 = Rectangle(10, 20)
print(rectangle_1.calculate_perimeter())

square_1 = Square(20, 20)
print(square_1.calculate_perimeter())