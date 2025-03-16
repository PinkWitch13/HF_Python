import random

"""1. Print three different strings."""
print('Hello.')
print('My name is Luna the Cat.')
print("I'm fluffy and I love to sleep.")


"""2. Write a program that prints a message if a variable is less than 10, 
    and a different message if the variable is greather than or equal to 10."""

variable = random.randint(0, 30)

if variable < 10:
    print("Oh boy, that's not much.")
else:
    print("Oh boy, that's a lot!")


"""3. Write a program that prints a message if a variable is less than or equal to 10,
    another message if the variable is greather than 10 but less than or equal to 25,
    and another message if the variable is greather than 25."""

if variable <= 10:

    print("Oh boy, it's not much")
elif variable > 10 and variable <= 25:
    print("Oh boy, that should be fine.")
else:
    print("Oh boy, that's a lot!")


"""4. Create a program that divides two variables and prints the reminder."""

rem = 25 % 4
print(rem)


"""5. Create a program that takes two variables, divides them, and prints the guotient"""

quo = 25 // 4
print(quo)


"""6. Write a program with a viariable age assigned to an integer that prints different strings  
    depending on what integer age is."""

age_variable = random.randint(0, 120)

if age_variable <= 10:
    print("I'm a kid.")
elif age_variable > 10 and age_variable <= 19:
    print("I'm a teenager.")
elif age_variable > 19 and age_variable <= 59:
    print("I'm an adult.")
elif age_variable > 59 and age_variable <= 99:
    print("I'm old.")
else:
    print("Wow! I should be dead but I'm not! XD")