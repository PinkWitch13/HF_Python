"""Implement a function to calculate the sum 
    of the numerical values in a nested list. """

lst = [1, [2, [3, [4]]]]

def sum_nested(lst):
    total = 0
    for l in lst:
        if isinstance(l, list):
            total += sum_nested(l)
        else:
            total += l
    return total

print(sum_nested(lst))