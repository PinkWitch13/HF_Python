#!/usr/bin/python3

#create a new list 'vowels' containing string objects (vowels)
vowels = ['a', 'e', 'i', 'o', 'u']
# 
word = input("Provide a word to search for vowels: ")
#create an empty dictionary named 'found'
found = {}


#for all letters in 'word', check if there are any vowels - if any found, count them
for letter in word:
    if letter in vowels:
        found[letter] += 1
        #found[letter] = found[letter] +1
       


#display on screen sorted list of vowels and how many times they where found in given 'word' (key/value pairs)

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'ime(s).')

    
