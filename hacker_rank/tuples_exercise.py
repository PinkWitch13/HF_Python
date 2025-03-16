"""Given an integer n, and n space-separated integers as input, create a tuple t, 
    of those n integers. Then compute and print the result of hash(t).  """

if __name__ == '__main__':
    n = int(input())
    m = list(input().split(' '))

l =[]

for n in range(0, n):
    nn = int(m.pop(0))
    l.append(nn)
t = tuple(l)

print(hash(t))

#amount_of_numbers = 2 # int(input())
#start_numbers = tuple([1, 2]) # str(tuple(input().split(' ')))

# amount_of_numbers = int(input())
# start_numbers = tuple(int(number) for number in input().split(' '))

# print(amount_of_numbers, start_numbers)


# print(hash(start_numbers))
