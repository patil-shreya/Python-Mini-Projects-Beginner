import random

from art import logo 

from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards = []
computer_cards =[]

def first_selection():
    for _ in range(2):
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards)) 

def another_card(user_score):
    next_card = random.choice(cards)
    if next_card == 11:
        if user_score > 10:
            next_card = 1
    your_cards.append(next_card)

def final_result(user_score, dealer_score):
    while dealer_score < 17:
        next_card = random.choice(cards)
        if next_card == 11:
            if dealer_score > 10:
                next_card = 1   
        computer_cards.append(next_card)
        dealer_score = sum(computer_cards)
    print(f"    Your final hand: {your_cards}, Final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, Final score: {dealer_score}")
    if user_score == dealer_score:
        return print(" Draw 🙃") 
    elif user_score > 21:
        return print(" You went over. You loose 😤")
    elif dealer_score > 21:
        return print(" Computer went over. You win 🥳")
    elif user_score == 21:
        return print(" Win with a Blackjack 😎") 
    elif dealer_score == 21:
        return print(" Loose, opponent has a Blackjack 😱") 
    elif user_score > dealer_score:
        return print(" You have the bigger hand. You win 😃")
    elif user_score < dealer_score:
        return print(" Computer has the bigger hand. You loose 😟") 

play_game = True
while play_game:
    want_to_play = input("  Do you want to play game of Blackjack? Type 'y' or 'n'.: ")
    if want_to_play == "n":
        play_game = False
    else:
        clear()
        print(logo)
        your_cards = []
        computer_cards =[]
        your_score = 0
        computer_score = 0
        first_selection()
        your_score = sum(your_cards)
        computer_score = sum(computer_cards)
        print(f"    Your cards: {your_cards}, Current score: {your_score}")
        print(f"    Computer's first hand: {computer_cards[0]}")
        continue_playing = True
        while continue_playing:
            want_to_continue = input("  Type 'y' to get another card, type 'n' to pass.: ")
            if want_to_continue == "n":
                continue_playing = False
                final_result(user_score=your_score, dealer_score=computer_score)
            else:
                another_card(user_score=your_score)
                your_score = sum(your_cards)
                computer_score = sum(computer_cards)
                print(f"   Your cards: {your_cards}, Current score: {your_score}")
                print(f"   Computer's first hand: {computer_cards[0]}")
