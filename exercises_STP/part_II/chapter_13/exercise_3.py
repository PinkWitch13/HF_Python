"""3. Create a class called Shape. Define a method 
    in it called what_am_i that prints "I am a 
    shape" when called. change your Square and 
    Rectangle classes from the previous challenges 
    to inherit from Shape, create Square and 
    Rectangle objects, and call the new method 
    on both of them.  """

class Shape:
    def __init__ (self, w, l):
        self.width = w
        self.len = l

    def what_am_i(self):
        print(f"Im a shape {self}")

class Rectangle (Shape):
    def calculate_perimeter(self):
        return (self.width*2)+(self.len*2)
    
class Square (Rectangle):
    pass

square_1 = Square(20, 20)
rectangle_1 = Rectangle(20, 30)

rectangle_1.what_am_i()
square_1.what_am_i()