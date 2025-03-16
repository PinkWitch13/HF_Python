#assuming the data is passed to function by value:
def double(arg):
    print('Before: ', arg)
    agr = arg *2
    print('After: ', arg)

#assuming the data is passed o function by reference:
def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After" ', arg)