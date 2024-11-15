# Dice Roller Assessment Python File 
#  Bkah bkah bkah 
# Need to import parts/ part of it to Main.Py 

import sys
import random as rnd 


def roll_dice (sides):
    num = rnd.randint(1, sides)
    return num

def Input_dice():
    D_Sid = input("How Many Sides do you want the Dice to Have? > ")
    D_Sid = int(D_Sid)
    D_Rol = input("How Many Dice Would you Like to Roll? > ")
    D_Rol = int(D_Rol)
    return (D_Sid, D_Rol)


def Argv_Dice():
    D_Sid = sys.argv[1]
    D_Sid = int(D_Sid)
    D_Rol = sys.argv[2]
    D_Rol = int(D_Rol)
    return (D_Sid, D_Rol)


arg_count = len(sys.argv) 
if arg_count > 1:
    output_dice = Argv_Dice()
else: 
    output_dice = Input_dice()

D_Rol = output_dice[1]
for roll in range(D_Rol):
    D_Anw = roll_dice(output_dice[0])
    print(f"The Result is {D_Anw}")
