""" 1. A recursive algorythm must have a base case.
    2. A recursive algorythm must change its state 
    and move toward the base case.
    3. A recursive algorythm must call itself, 
    recursively.  """

"""  99 Bottles of Beer on the Wall  """

def bottles_of_beer(bob):
    if bob< 1:
        print(""""No more bottles of beer on the wall 
              No more bottles of beer.""")
        return 
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {}
          bottles of beer. Take one down, pass it 
          around, {} bottles of beer on the wall.
          """.format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(99)