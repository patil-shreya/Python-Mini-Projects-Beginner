import random
import art
from game_data import data
from replit import clear

print(art.logo)

def console_clear():
    clear()
    print(art.logo) 

first_data = random.choice(data)
your_score = 0

am_playing = True
while am_playing:
    print(f"Compare A: {first_data['name']}, {first_data['description']}, from {first_data['country']}.") 
    print(art.vs)
    next_data = random.choice(data)
    print(f"Against B: {next_data['name']}, {next_data['description']}, from {next_data['country']}.") 
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower() 
    if user_choice == "a":
        if first_data['follower_count'] > next_data['follower_count']:
            first_data = next_data
            your_score += 1
            console_clear()
            print(f"You are right! Your Score: {your_score}")  
        else:
            console_clear()
            print(f"Sorry thats wrong. Final score: {your_score}")
            am_playing = False
    elif user_choice == "b":
        if first_data['follower_count'] < next_data['follower_count']:
            first_data = next_data
            your_score += 1
            console_clear()
            print(f"You are right! Your score: {your_score}")
        else:
            console_clear()
            print(f"Sorry thats wrong. Final score: {your_score}")
            am_playing = False
