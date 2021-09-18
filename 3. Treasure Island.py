print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("To get home safe and sound you gotta complete a mission.")
print("Your mission is to find the treasure.") 
print("Are you ready??!!!")
print("LETS START!!")
print("You are walking down a path and come across two roads, one goes to the left and the other goes to the right.")
road_choice = input("Which road do you choose to go? Left or Right?").lower()
if road_choice == "left":
    print("You are safe. CONTINUE!")
    print("Moving forward you come across a river.You have two options to cross the river. Either swim or wait for the boat.")
    river_choice = input("What do you choose? Swim or Wait?").lower()
    if river_choice == "wait":
        print("You safely crossed the river. Congragulations!!!")
        print("After successfully crossing the river now you are the last level.")
        print("You see three doors infront of you blue, yellow and red. You have to go through one to find the treasure.")
        door_choice = input("Which door do you choose? Blue, Red or Yellow?").lower()
        if door_choice == "yellow":
            print("HURRAYYY!!! You found the hidden treasure. You Won!! Congragulations!!!!!")
        elif door_choice == "red":
            print("OOPS!!! It was a room of fire. You got burned. Better luck next time. GAME OVER!!")
        elif door_choice == "blue":
            print("Oh Sorry!! It was a room full of beasts and you became their meal. Better luck next time. GAME OVER !!!")
        else:
            print("You went out of range. GAME OVER!!!")
    elif river_choice == "swim":
        print("OMG!! You became food for the crocodiles. Better luck next time!!")
    else:
        print("You went out of range. GAME OVER!!!")
elif road_choice == "right":
    print("OOPS!!! You fell into a hole. GAME OVER!!!")    
else:
    print("You went out of range. GAME OVER!!")
