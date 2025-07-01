""" Define a function that removes duplicates from an array 
    of non negative numbers and returns it as a result.
    The order of the sequence has to stay the same. """

seq = [1, 2, 1, 1, 3, 2]

def distinct(seq):
    uniq = []
    for num in seq:
        if num not in uniq:
            uniq.append(num)
    return uniq

print(distinct(seq))

