"""Write a program that prints the numbers from 1 to 100 
    But for multiples of three print  "Fizz" insted of the 
    number, and for the multiple of five print  "Buzz"  . 
    For multiplies of both three and five print  "FizzBuzz".  """

def fizz_buzz ():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
       
fizz_buzz()