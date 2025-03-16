"""2. Change the Square class so that when you 
    print a Square object, a message prints 
    telling you the len of each of the four 
    sides of the shape. For example, if you 
    create a square with Square(29) and print 
    it, Python should prnt 29 by 29 by 29 
    by 29.  """

class Square:
    list_squares = []

    def __init__ (self, l):
        self.len = l
        self.list_squares.append(self.len)

    def __str__ (self):
        return("""square with sides {} by {} by {} by {}
              """.format(self.len,
                         self.len,
                         self.len,
                         self.len))
        
square_1 = Square(29)
print(square_1)