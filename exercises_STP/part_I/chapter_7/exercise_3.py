from exercise_1 import shows
"""3. Print each item in the list from the first challenge 
   and their indexes.  """

# shows = ["The Walking Dead", "Entourage", 
#          "The Sopranos", "The Vampire Diaries"]

for i, each_show in enumerate(shows):
    print(f"{each_show} have index {i}.")


