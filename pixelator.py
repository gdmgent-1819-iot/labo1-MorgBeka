from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

limited = range(0,8)

def repeat():
    for i in limited:
        for j in limited:
            color = (randint(0,255), randint(0,255), randint(0,255))
            sense.clear()
            sense.set_pixel(i,j, color)
            time.sleep(1)
    repeat()
repeat()
