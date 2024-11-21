from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
#blafhg 
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "Coin"


def select_face_option(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    dice_type = document.getElementById("D_sid").value
    print(dice_type)


def roll_all_dice(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    dice_roll = document.getElementById("D_Rol").value 
    dice_roll=int(dice_roll)
    dice_num = 0 
    if dice_type == "D2":
        dice_num = 2 
    elif dice_type == "D4":
        dice_num == 4
    elif dice_type == "D6":
        dice_num == 6
    elif dice_type == "D8":
        dice_num == 8
    elif dice_type == "D10":
        dice_num == 10
    elif dice_type == "D12":
        dice_num == 12
    elif dice_type == "D20":
        dice_num == 20 
    elif dice_type == "D100":
        dice_num == 100
    output="the dice roll is > "
    print(f"number: {dice_num}")
    for roll in range(dice_roll):
        #D_res = dice.roll_dice(dice_num)
        #output = f"{output}, {D_res}"
        ...

    document.querySelector("div#roll-history").innerHTML = output


def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""
