from datetime import datetime
"""First I have to import the datetime module which supplies classes for manipulating dates and times.
I create a new variable 'odds' which is a list of elements related to odd minutes.
for a new variable 'right_this_minute' replies to a today() class and """ 
odds=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
right_this_minute=datetime.today().minute
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")


help(datetime.today())
