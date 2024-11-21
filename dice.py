# Dice Roller Assessment Python File 
#  Bkah bkah bkah 
# Need to import parts/ part of it to Main.Py 
#pyclick is needed to input stuff from html to the python script, it takes the place of onclick, but due to it being Java based, py-click is used instead
import sys
import random as rnd 


def roll_dice (sides):
    num = rnd.randint(1, sides)
    return num