"""You are given a string S.
    Your task is to find out if the string S 
    contains: alphanumeric characters, 
    alphabetical characters, digits, 
    lowercase and uppercase characters.  
    
    Output:
    In the first line, print True if S has 
    any alphanumeric characters. Otherwise, 
    print False.
    In the second line, print True if S has 
    any alphabetical characters. Otherwise, 
    print False.
    In the third line, print True if S has 
    any digits. Otherwise, print False.
    In the fourth line, print True if S has 
    any lowercase characters. Otherwise, 
    print False.
    In the fifth line, print True if S has 
    any uppercase characters. Otherwise, 
    print False."""

if __name__ == '__main__':
    s = input()

s_listed = list(s)

alphanum = 0
alpha = 0
dig = 0
lower = 0
upper = 0

for digits in s_listed:
    if digits.isalnum() == True:
        alphanum += 1
    if digits.isalpha() == True:
        alpha += 1  
    if digits.isdigit() == True:
        dig += 1
    if digits.islower() == True:
        lower += 1
    if digits.isupper() == True:
        upper += 1
    else:
        continue

types = [alphanum, alpha, dig, lower, upper]

for type in types:
    if type != 0:
        print(True)
    else:
        print(False)


# types = []
# types.append([alphanumeric, alphabetical, \
#               digits, lower, upper
#               ])

# def string_validator(types):
#     for type in types:
#         print(type)

# string_validator(types)
