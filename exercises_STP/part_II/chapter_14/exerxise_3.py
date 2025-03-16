"""3. Write a function that takes two objects 
    as a parameters and returns True if they 
    are the same object, and False if not.  """

cat_1 = "Luna"
cat_2 =  "Luna"  #"Zoya"


def same_or_not(cat_1, cat_2):   
    if cat_1 == cat_2:
        print(True)
    
    else:
        print(False)

      
same_or_not(cat_1, cat_2)