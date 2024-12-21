from datetime import datetime
odds=list(range(1,59, 2))
time_now = datetime.today()
right_this_minute  = time_now.minute
if right_this_minute in odds:
    print("This minute seem a little odd.")
else:
    print("Not an odd minute.")
