import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if player_choice == 0:
    print(rock)
    print("Computer chose:")
    if computer_choice == 0:
        print(rock)
        print("Its a draw")
    elif computer_choice == 1:
        print(paper)
        print("You loose")
    else:
        print(scissors)
        print("You won")
elif player_choice == 1:
    print(paper)
    print("Computer chose:")
    if computer_choice == 0:
        print(rock)
        print("You won")
    elif computer_choice == 1:
        print(paper)
        print("Its a draw")
    else:
        print(scissors)
        print("You loose")
elif player_choice == 2:
    print(scissors)
    print("Computer chose:")
    if computer_choice == 0:
        print(rock)
        print("You loose")
    elif computer_choice == 1:
        print(paper)
        print("You won")
    else:
        print(scissors)
        print("Its a draw")
else:
    print("Invalid Input!!")





