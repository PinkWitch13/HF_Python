import re

"""2. Come up with a regular expression 
    that matches all the digits in the 
    string  Arizona, 479, 501, 870. 
    California 209, 213, 650.  """

string_to_investigate = "Arizona, 479, 501, 870. California 209, 213, 650."

match = re.findall("\d",
                   string_to_investigate,
                   re.IGNORECASE)

print(match)