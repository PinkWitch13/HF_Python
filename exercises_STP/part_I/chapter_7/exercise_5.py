"""5. Multiply all the numbers in the list [8, 19, 148, 4] 
    with all the numbers in the list [9, 1, 33, 83], 
    and append each result to a third list. """

first_ls = [8, 19, 148, 4]
second_ls = [9, 1, 33, 83]

def num_multiplier (first_ls, second_ls):
    final_ls = []
    for first_num in first_ls:
        for second_num in second_ls:
            final_num = first_num * second_num
            final_ls.append(final_num)
    print(final_ls)

num_multiplier(first_ls, second_ls)