from art import logo

import random

def make_a_guess(user_guess, actual_number):
    if user_guess == actual_number:
        return print(f"You've got it!! The answer was {actual_number}.")
    elif user_guess < actual_number:
        return print("Too Low")
    elif user_guess > actual_number:
        return print("Too high")


print(logo)

numbers = []

for _ in range(1, 101):
    numbers.append(_)

chosen_number = random.choice(numbers)

print("Welcome to the Number Guessing Game!!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.: ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

game_continue = True

while game_continue:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    make_a_guess(user_guess=guess, actual_number=chosen_number)
    if guess == chosen_number:
        game_continue = False
    elif guess != chosen_number:
        attempts -= 1
        if attempts == 0:
            game_continue = False
            print("You've run out of guesses. You loose.") 
        else:
            print("Guess again") 


