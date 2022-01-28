# Scope

# Local Scope - a local variable/function exists only within the block that it is declared in
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength)  # NameError: potion_strength is not defined

# Global Scope - a global variable/function exists only once in a script and is visible in every function
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        boost_health = potion_strength + player_health
        print(boost_health)

    drink_potion()


game()
print(player_health)

# As a rule, use different names for global and local variables.

# Global Constants
# The naming convention is to use uppercase letters to remember not to change them but it does not prevent reassignment.
PI = 3.14159

# Modifying Global Scope
enemies = 1


def increase_enemies():
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

# There is no Block Scope in Python
game_level = 3
enemies = ["Skeleton'", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]  # New variable created in if statement returns no error
print(new_enemy)

# Day 12 Project - Number Guessing Game
from random import randint
from number_guessing_game_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = randint(1, 100)

# print(f"Pssst, the correct answer is {number_to_guess}.")

level_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number_of_guesses = 0
if level_difficulty == "easy":
    number_of_guesses = 10
elif level_difficulty == "hard":
    number_of_guesses = 5

while number_of_guesses > 0:
    found_the_number = False
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    if player_guess > number_to_guess:
        print("Too high.")
        number_of_guesses -= 1
        if number_of_guesses > 0:
            print("Guess again.")
    elif player_guess < number_to_guess:
        print("Too low.")
        number_of_guesses -= 1
        if number_of_guesses > 0:
            print("Guess again.")
    elif player_guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}.")
        number_of_guesses = 0
        found_the_number = True

if found_the_number is False:
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
    print(f"The number to guess was {number_to_guess}.")

# Angela's solution
from random import randint
from number_guessing_game_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

    # Let the user guess a number.
    guess = int(input("Make a guess: "))

    # Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")
        return
    elif guess != answer:
        print("Guess again.")


game()
