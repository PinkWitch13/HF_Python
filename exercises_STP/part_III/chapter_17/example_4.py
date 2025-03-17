import re

l = "Beautiful is better than ugly."

matches = re.findall("Beautiful", l)

""" or to make it case insensitive: """

matches = re.findall("beautiful",
                     l,
                     re.IGNORECASE)
print(matches)