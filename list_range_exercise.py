
nrth = "    |"
nrth_east = "  /"
east = ".---"
sth_east = "  \\"
sth = "    |"
sth_wst = "  /"
wst = " --"
nrth_wst = "  \\"

print(nrth)
print(north_west, north_east)
print(west, east)
print(south_west, south_east)
print(south)

current_time = datetime.datetime.now()
print("Current time in Warsav is:", current_time)

#index 0         1       2       3       4      5      6     7
tic = [nrth, nrth_east, east, sth_east, sth, sth_wst, wst, nrth_wst]
print(tic[::2])
print(tic[::1])
print(tic[::-1])

print(nrth)
print(north_west, north_east)
print(west, east)
print(south_west, south_east)
print(south)





