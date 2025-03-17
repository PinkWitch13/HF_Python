import re

"""1. Write a regular expression that matches 
    the word Dutch in The Zen of Python.  """

with open("zen.txt", "r") as zen:
    
    content = zen.read()
    
    match = re.findall("Dutch",
                       content,
                       re.MULTILINE)
    
    print(match)


