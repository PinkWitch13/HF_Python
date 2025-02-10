n = int(input("How many hotdogs?: "))
if n < 5:
    price = n *100
else:
    if n >=5 and n < 10:
        price = n * 95
    else:
        price = n * 90
print(price)