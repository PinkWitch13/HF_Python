"""1. Add a square_list class variable to a class 
    called Square so that every time you create a 
    new Square object, the new object gets added 
    to the list.  """

class Square:
    square_list = []

    def __init__ (self, side):
        self.side = side
        self.square_list.append(self.side)

square_1 = Square(20)

print(square_1.square_list)
        