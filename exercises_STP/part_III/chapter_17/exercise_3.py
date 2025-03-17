import re

"""3. Create a regular expression that matches 
    any word that starts with any character and 
    is followed by two o's. Then use Python's re 
    module to match boo and loo in the sentence
    The ghost that says boo hounts the loo.  """

sentence = "The ghost that says boo hounts the loo."
   
found = re.findall(".oo",
                   sentence,
                   re.IGNORECASE)
print(found)
