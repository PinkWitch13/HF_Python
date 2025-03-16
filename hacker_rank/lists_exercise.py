"""Consider a list (list = []). 
    You can perform the following commands:
    insert i e: Insert integer  at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer .
    append e: Insert integer  at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
    Initialize your list and read in the value of  followed by 
    lines of commands where each command will be of the 
    types listed above. Iterate through each command in order 
    and perform the corresponding operation on your list.  """

if __name__ == '__main__':
    N = int(input()) 

lst = []


for types in range(0,N):
    print('Avaible commands: insert, print, remove, \
          append, sort, pop, reverse')
    n = input('Please type command: ').split(' ')
    if 'insert' in n:
        i = int(n.pop(1))
        e = int(n.pop(1))
        lst.insert(i, e)
        print(lst)
    elif 'print' in n:
        print(lst)
    elif 'remove' in n:
        e = int(n.pop(1))
        lst.remove(e)
        print(lst)
    elif 'append' in n:
        e = int(n.pop(1))
        lst.append(e)
        print(lst)
    elif 'sort' in n:
        lst.sort()
        print(lst)
    elif 'pop' in n:
        lst.pop()
    elif 'reverse' in n:
        lst.reverse()
        print(lst)
    else:
        print('Wrong input!')