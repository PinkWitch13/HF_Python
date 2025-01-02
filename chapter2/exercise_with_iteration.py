#Assign given string value to he variable 'book'.
#Then create a new list called 'booklist', which includes each letter object from 'book'.
#Finally display 'booklist' on the screen.

book = "The Hitchhiker's Guide to Galaxy"
booklist = list(book)
print(booklist)

#from 'booklist' select and display first three elements.
booklist[0:3]

#Turn selected objects ito the string.
"""indexes in range 0 - 36 (from the first to the last sign in quote)"""
''.join(booklist[0:3])
"""indexes in range -1 - -36 (from the last to the first sign).
In this example range is set with start on -6 and end on -1,
so the string will be created from the last 6 elements"""
''.join(booklist[-6:])

#create a new list 'backwords', containing all elements from booklist but in reversed order.
backwords = booklist[::-1]
#join all the elements in 'backwords' into a string and display it.
''.join(backwords)

#create a new list 'every other', containing every second object from booklist.
every_other = booklist[::2]
#join all the elements in 'every other' into a string and display it.
''.join(every_other)

#slice out word 'Hitchhiker' 
''.join(booklist[4:14])
#slice out word 'Hitchhiker' but backword 
''.join(booklist[13:3:-1])
