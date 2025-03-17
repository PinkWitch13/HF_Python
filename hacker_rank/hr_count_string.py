import re

""""EXERCISE: In this challenge, the user enters a string and 
    a substring. You have to print the number of times that 
    the substring occurs in the given string. String traversal 
    will take place from left to right, not from right to left.  """

main_str = 'CDDC' #'Kuba jest fajny' #ABCDCDC' 
sub_str = 'CDC' #'Kuba' #'CDC' 
count = 0

found = re.findall(sub_str, main_str)





# def count_substring(main_str, sub_str):
#     counter = 0
#     sub_str = list(sub_str)
#     let_count = 0
#     ch_count = 0
#     for letter in main_str:
#         if letter in sub_str:
#            ch_count += 1
#            print(f'{let_count=}')
#            if ch_count == len(sub_str) and let_count == len(sub_str):
#                 counter += 1
#                 let_count = 0
#                 ch_count = 0
#                 continue
#            elif ch_count < len(sub_str) and let_count < len(sub_str):
#                 let_count += 1
#                 continue
#            elif ch_count > len(sub_str):
#                 let_count = 0
#                 continue
#         else:
#             ch_count -=1
#             let_count = 0
#             continue
#     return counter

# def count_substring(main_str, sub_str):
#     let_count = 0
#     counter = 0
#     sub_str = list(sub_str)
#     for letter in main_str:
#         if letter in sub_str:
#             let_count += 1
#             if let_count == len(sub_str):
#                 counter += 1
#                 let_count = 0
#                 continue
#             elif let_count < len(sub_str):
#                 continue
#         elif letter not in sub_str:
#             let_count = 0
#             break
#     return counter

# print(f'Substring occured {count_substring(main_str, sub_str)} times')