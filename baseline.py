from sense_hat import SenseHat
import time 
sense = SenseHat()
sense.rotation = 90
from random import randint


hello = ["Hello! We are New Media Development :)"]

def repeat():
    for i in hello:
        color = (randint(0,255), randint(0,255), randint(0,255))
        background_color =(randint(0,50), randint(0,50), randint(0,50))
        sense.show_message(i, text_colour = color, back_colour = background_color)
        time.sleep(1)
    repeat()

repeat()
