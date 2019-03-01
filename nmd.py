from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
sense.clear()

word = ["N", "M", "D"]

def repeat():
    for i in word:
        color = (randint(0,255), randint(0,255), randint(0,255))
        sense.show_letter(i, text_colour = color)
        time.sleep(1)
    repeat()

repeat()
    
