import random

"""2. Define a method in your Square class 
called change_size that allows you to pass 
in a number that increases or decreases 
(if the number is negative) each side of a 
Square object by that number.  """

number = int(input('Give a number: '))

class Rectangle():
    def __init__ (self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width*2)+(self.len*2)
    
class Square (Rectangle):
    def change_size (self):
        self.width = self.width + number
        self.len = self.len + number
        return self.width, self.len

square_1 = Square(20, 20)
print(square_1.change_size())
