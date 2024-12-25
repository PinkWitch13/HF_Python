#!/usr/bin/python3

#above command allows me to run python program directly form linux command line <3
#to varible 'vowels' assign a list of literals
vowels = ['a', 'e', 'i', 'o', 'u']
#assign providet by user specified input to variable 'word'
word = input("Provide a word to search for vowels: ")
#create an (temporary) empty list and assign it to the variable 'found'
found = []
#make a loop and repeat for every letter in given word
for letter in word:
#check every letter if it's a part of 'vewels'... 
    if letter in vowels:
#if cannot find letter on the list 'found', add letter to this list.
        if letter not in found:
            found.append(letter)
#commpare if elements from the list 'vowel' are also included in list 'found', and display 'vowel' on screen
for vowel in found:
    print(vowel)
    
