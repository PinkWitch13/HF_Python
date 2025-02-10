
"""create an empty dict named 'fruits'"""
fruits = {}
"""to key value 'apples' assign value 10, add this pair to 'fruits'"""
fruits['apples'] = 10
"""check if 'fruits' contain key value 'apples', if not - assign to 'apples' value 1, and add this pair to 'fruits'"""
if 'apples' in fruits:
    print(True)
else:
    fruits['apples'] = 1

"""check if fruits contain 'bananas' key, if so- add +1 to 'bananas' value, if not- add 'bananas' with assigned value 1 to 'fruits'"""     
if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1

"""when I run above code second time, else condition is selected, as 'bananas' are alredy in 'fruits'.
If I use print on 'fruits', I'll see the value of 'bananas' was increst by 1 (Python displays value 2 for 'bananas')."""
if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1


"""Check if 'fruits' are not containing 'pears', if so - add 'pears' with value set on 0 to 'fruits.
Otherwise increse 'pears' value by 1.'"""
if 'pears' not in fruits:
    fruits['pears'] = 0
else:
    fruits['pears'] += 1    
print(fruits)
"""When I use print on 'fruits', I'll see the value for 'pears' is set to 1.
If I increase 'pears' value by 1 and use print on fruits again I'll see displayed value of 'pears' is 2 """
fruits['pears'] =+ 1
print(fruits)


"""to shorten my code I can use on 'fruits' setdefault method instead,
with given argument 'pears' and its value set to 0. Method adds given argument with specified value to dict.
If I then increase 'pears' value by 1, and then use print on 'fruits' ill see the displayd value of 'pears' is 2"""
fruits.setdefault('pears', 0)
fruits['pears'] += 1
print(fruits)
