class AlwaysPositive:
    def __init__ (self, number):
        self.n = number

    def __add__ (self, other):
        return abs(self.n + other.n)

"""abs is a build-in function return the absolute value"
    of two numbers added togheter in an expression. """

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)