"""Given a string containing a list of integers 
    separated by commas, write the function that 
    takes said string and returns a new array / 
    list containing all integers present in the 
    string, preserving the order.

    Please note that there can be one or more consecutive 
    commas whithout numbers, like so:
    
    '-1,-2,,,,,,3,4,5,,6' """

s = "1,2,3,,,4,,5,,,"

def string_to_int_list(s):
    l = s.split(',')
    print(l)
    num_l = []
    for element in l:
        if type(element) == int:
            num_l.append(element)
        else:
            continue
    return num_l

print(string_to_int_list(s))

