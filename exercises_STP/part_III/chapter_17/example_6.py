import re

zen = """Although never is
often better than
*right8 now.
If the implementation
is hard to explain, 
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking 
great idea -- let's 
do more of those!
"""

m = re.findall("^If",
               zen,
               re.MULTILINE)

print(m)

""" passing re.MULTILINE as a third parameter to findall make
    it to look for matches on all of the lines of a multi-line string.  """