"""assign string value 'Don't panic!' to the variable 'phrase'"""
phrase = "Don't panic!"
"""create new list 'plist', containing every sighn from the string value 'phrase'"""
plist = list(phrase)
"""display 'phrase' on screen"""
"""display 'plist' on screen"""
print(phrase)
print(plist)

#display featured elements on the screen, each on its own but on the same line (so it is not the right answer)
print(plist[1], plist[2], plist[5], plist[4], plist[7], plist[6])

#join second and third element from plist into a new string named 'new_phrase',
#then extend this string by adding values from specified elements
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

"""display plist and new_phrase"""
print(plist)
print(new_phrase)
