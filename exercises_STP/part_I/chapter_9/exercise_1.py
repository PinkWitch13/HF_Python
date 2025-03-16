"""1. Find a file on your computer and print 
    its content using Python. """

my_text = []

with open("Diuna.txt", "r") as diuna:
    my_text.append(diuna.read())

print(my_text)