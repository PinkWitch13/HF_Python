from datetime import datetime
import random
import time

odds= list(range(1, 60, 2))
for i in range (5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
        wait_time = random.randint(1, 60)
        time.sleep(wait_time)
        
