from datetime import datetime
#odds = list(range(1, 59, 2))
#time_now = datetime.today()
#for every_minute in time_now:
#    every_minute = datetime.today().minute
#    if every_minute in odds:
#        print("This minute seem a little odd.")
#    else:
#        print("Not an odd minute.")



odds = list(range(1, 59, 2))

rigth_time_now = datetime.today().minute

if rigth_time_now in odds:
        print("This minute seem a little odd.")
else:
        print("Not an odd minute.")
