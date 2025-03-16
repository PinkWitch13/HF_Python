import math
import random

"""2. Create a Circle class with a method 
    called area that calculates and returns 
    its area. Then create a Circle object, 
    call area on it, and print the result. 
    Use Python's pi in the build-in math 
    module.  """

pi = math.pi
input_radius = random.randint(0,10)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (pi*(self.radius)**2)
    
circle_1 = Circle(input_radius)
print(circle_1.area())
