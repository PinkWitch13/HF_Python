import random

n= random.randint(0, 20)
stairs = list(range(0, n))

for s in stairs:
    width = "\t" * s
    tall = "\n" * s
    step = "I"
    
    
