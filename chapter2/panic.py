phrase = "Don't panic"
plist = list(phrase)
new_plist = []
print(plist)
for phrase in plist:
    print(phrase)
    if phrase not in new_plist:
        new_plist.extend(phrase)
        print(new_plist)
    else:
        for phrase in new_plist:
            pass
        
        
        
#my code
#new_phrase = []
#new_phrase= ["", "'"].join(phrase)
#print(new_plist)
#print(new_phrase)
