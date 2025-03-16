import random

"""3. Create a Triangle class with a method 
    called area that calculates and returns 
    its area. Then create Triangle object, 
    call area on it, and print the result.  """

ran_1 = random.randint(0, 20)
ran_2 = random.randint(0, 20)

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return 0.5 * self.base * self.height
    
triangle_1 = Triangle(ran_1, ran_2)

print(triangle_1.area())

