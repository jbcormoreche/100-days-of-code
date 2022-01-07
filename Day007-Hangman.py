# Hangman
import random
from hangman_art import logo, stages
from hangman_words import word_list

# Start the game
print(logo)
game_is_finished = False
lives = len(stages) - 1

# Pick a random word from the list in hangman_word.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code.
# print(f"Pssst, the solution is {chosen_word}.")

# For each letter in the chosen_word, add a "_" to a list called display.
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}\n")

# Ask the user to guess a letter, assign their answer to a variable and make it lowercase.
# Use a while loop to let the user guess again.
while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"\nYou've already guessed the letter {guess}.")
        print(f"\n{' '.join(display)}")
    else:
        # Loop through each position in the chosen_word.
        # If the letter at that position matches the guess then reveal that letter in the display at that position.
        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                print(f"\nThe letter {guess} is in the word.\n")
                display[position] = letter
                print(f"{' '.join(display)}")

        if guess not in chosen_word:
            lives -= 1
            print(f"\nThe letter {guess} is not in the word, you have {lives} lives left.")
            print(f"\n{' '.join(display)}")
            if lives == 0:
                game_is_finished = True
                print("\nYou lose.")
                print(f"\nThe word was {chosen_word}.")

        # The loop stops once the user has guessed all the letters in the chosen_word and the display has no more blanks ("_").
        if "_" not in display:
            game_is_finished = True
            print("\nYou guessed the word, you win!")

    # Print the ASCII art from hangman_art.py that corresponds to the current number of lives the user has remaining.
    print(stages[lives])
