import re

t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

for match in found:
    print (match)

"""for non-greedy matching (that only finds the first occurence)
   .* follow by ? symbol"""