from  exercise_3 import about_me

"""4. Write a program that lets the user ask your 
    height, favorite colour, favorite author, and
    returns the result from the dictionary you created 
    in the previous program.  """

# about_me = {}
# about_me['height'] = '175cm'
# about_me['fav_colour'] = 'blue'
# about_me['fav_author'] = 'Frank Herbert'
# about_me['fav_animal'] = 'cat'

qestion = input()

if qestion in about_me:
    print(about_me[qestion])
else:
    print("Wrong question! Answer not found.")