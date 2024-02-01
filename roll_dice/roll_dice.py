import random

want_use = True
max_roll = 6
choices = ["roll", "change", "quit"]

print("Hi, this is a realy simple dice roll app.")
change = input("Standard max roll = 6 to work use comands: (change, roll, quit): ")

while want_use == True: #main

    print("Max roll = " + str(max_roll))
    if change in choices == False:
        print("ERROR!!!")
        change = input("PLEASE ENTER: [roll, change or quit]: ")
        break

    while change == "roll": #dice roll
        dice_roll = random.randint(0, max_roll)
        print("Your roll is: " + str(dice_roll))
        change = input("What next? ")

    while change == "change": #change max roll
        max_roll = input("Enter max roll: ")
        if max_roll.isdigit() == False:
            print("USE ONLY NUMBERS!!!")
            continue
        else:
            max_roll = int(max_roll)
            change = "roll"

    while change == "quit": #stop app
        want_use = False
        print("exit")
        break
