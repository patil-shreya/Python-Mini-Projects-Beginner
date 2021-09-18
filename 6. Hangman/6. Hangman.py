import random
import hangman_words
import hangman_art

end_of_game = False

chosen_word = random.choice(hangman_words.word_list)

lives = 6

print(hangman_art.logo)

display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
                print(f"You have already guessed the letter {guess}.") 

    for n, letter in enumerate(chosen_word):
        if letter == guess:
            display[n] = letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, the letter is not in the word. You loose a life.") 
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
