"""Your task is to make two functions 
   ( max and min, or maximum and minimum, 
   etc., depending on the language ) that 
   receive a list of integers as input, 
   and return the largest and lowest 
   number in that list, respectively. 
   Each function returns one number. """

arr = [4,6,2,1,9,63,-134,566]

def minimum(arr):
    min_num = min(arr)
    return min_num

def maximum(arr):
    max_num = max(arr)
    return max_num

print(minimum(arr))
print(maximum(arr))

#rewrite both functions with iteration instead of max and min