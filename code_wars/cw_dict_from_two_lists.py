"""There are two lists, possibly of different lengths. 
    The first one consists of keys, the second one consists 
    of values. Write a function createDict(keys, values) 
    that returns a dictionary created from keys and values. 
    If there are not enough values, the rest of keys should 
    have a None (JS null)value. If there not enough keys, 
    just ignore the rest of values.   """

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

def create_dict(keys, values):
    l_dict = {}
    vlen = len(values)
    for i, key in enumerate(keys):
        if i < vlen:
            v = values[i]
            l_dict[key] = v
        else:
            v = None
            l_dict[key] = v
            
    print(l_dict)

create_dict(keys, values)
    

    