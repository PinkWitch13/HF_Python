""" In this kata, your job is to return the two distinct 
    highest values in a list. If there're less than 2 
    unique values, return as many of them, as possible.
    The result should also be ordered from highest to 
    lowest.  """

arg1 = [4, 10, 10, 9]

def two_highest(arg1):
    if not arg1:
        return []
    unique_numbers = set(arg1)
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[:2]

print(two_highest(arg1))