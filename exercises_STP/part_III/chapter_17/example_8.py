import re

string = "Two too."

m = re.findall("t[wo]o",
               string,
               re.IGNORECASE)

print(m)