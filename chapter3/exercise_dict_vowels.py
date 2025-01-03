#!/usr/bin/python3

#create a new list 'vowels' containing string objects (vowels)
vowels = ['a', 'e', 'i', 'o', 'u']
# 
word = input("Provide a word to search for vowels: ")
#create an empty dictionary named 'found'
found = {}
#to each vowel from 'vowels' assign value 0, creating key/value pairs for 'found'
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0


#for all letters in 'word', check if there are any vowels - if any found, count them
for letter in word:
    if letter in vowels:
        found[letter] += 1
        #found[letter] = found[letter] +1
       


#display on screen sorted list of vowels and how many times they where found in gven 'word' (key/value pairs)

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'ime(s).')

    
