import time
import random
from datetime import datetime

m = random.randint(1, 60)
odds = list(range(1, 59, 2))

for right_this_minute in range(m):
        rigth_this_minute = datetime.today().minute
        if rigth_this_minute in odds:
                print("This minute seem a little odd.")
                time.sleep(60)
        else:
                print("Not an odd minute.")
                time.sleep(60)
