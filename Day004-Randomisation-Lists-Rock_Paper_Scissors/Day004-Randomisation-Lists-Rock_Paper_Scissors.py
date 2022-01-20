# Randomisation and Lists

# Random module - Create a random integer
import random

random_integer = random.randint(1, 10)
print(random_integer)

# Create and use a module
# Make a separate file named my_module.py and add the line pi = 3.14159
import my_module

print(my_module.pi)

# Another way of importing a module
from my_module import pi

print(pi)

# Generate random floating point numbers in the interval [0, 1) (between 0 included and 1 not included)
random_float = random.random()
print("random_float")

# Generate random floating point numbers in the interval [0, 5)
random_float2 = random.random() * 5
print("random_float2")

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Interactive Coding Exercise - Heads or Tails
# Write a virtual coin toss program that randomly tells the user "Heads" or "Tails".
import random

random_integer = random.randint(0, 1)
if random_integer == 0:
    print("Tails")
else:
    print("Heads")

# Lists - Organize and store data

# Access an item in a list
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[0])

# Access an item starting from the end of a list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
print(states_of_america[-1])

# Replace an item in a list
fruits[1] = "Orange"
print(fruits)

# List append() method - Add an item to the end of a list
fruits.append("Banana")
print(fruits)

# Use the append() method if you want to add items to an empty list
vegetables = []
vegetables.append("Spinash")
print(vegetables)

# += is the shorthand symbol of the extend() method and returns a TypeError for empty lists

# List extend() method - Add multiple items to the end of a list
fruits.extend(["Lemon", "Blueberry"])
print(fruits)

# List remove() method - Remove the first matching element from a list
prime_numbers = [1, 2, 3, 5, 7, 8, 9, 11]
prime_numbers.remove(8)

# List sum() method - Add the items of a list and returns the sum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))

# List split() method - Break up a string at a specified separator and return a list of strings
string = "Hello,from,AskPython"
split_string = string.split(",")
print(split_string)

# Interactive Coding Exercise - Banker Roulette
# Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_of_people = len(names)
random_choice = random.randint(0, number_of_people - 1)
person_pay = names[random_choice]
print(f"{person_pay} is going to buy the meal today!")

# List random choice() method - Return a random element from a list
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
person_pay = random.choice(names)
print(f"{person_pay} is going to buy the meal today!")

# Nested lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])  # In the second nested list [1], "Kale" is the second item [1]

# Interactive Coding Exercise - Treasure Map
# Write a program that will mark a spot with an X.
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? (column)(row) "))
x_row = position[1] - 1
y_row = position[0] - 1
map[x_row][y_row] = "X"
print(f"{row1}\n{row2}\n{row3}")

# Day 4 Project - Rock Paper Scissors
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

print("Play the Rock Paper Scissors game.")
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Computer choice
computer_choice = random.randint(0, 2)

# Logic of the game
if your_choice < 0 or your_choice > 2:
    print("You typed an invalid number, you lose!")
else:
    if your_choice == computer_choice:
        who_wins = "It's a draw."
    elif your_choice == 0 and computer_choice == 2:
        who_wins = "You win!"
    elif your_choice == 1 and computer_choice == 0:
        who_wins = "You win!"
    elif your_choice == 2 and computer_choice == 1:
        who_wins = "You win!"
    elif your_choice == 0 and computer_choice == 1:
        who_wins = "You lose."
    elif your_choice == 1 and computer_choice == 2:
        who_wins = "You lose."
    elif your_choice == 2 and computer_choice == 0:
        who_wins = "You lose."

    # Text and art
    if your_choice == 0:
        your_choice_text = "Rock"
        your_choice_art = rock
    if your_choice == 1:
        your_choice_text = "Paper"
        your_choice_art = paper
    if your_choice == 2:
        your_choice_text = "Scissors"
        your_choice_art = scissors

    if computer_choice == 0:
        computer_choice_text = "Rock"
        computer_choice_art = rock
    if computer_choice == 1:
        computer_choice_text = "Paper"
        computer_choice_art = paper
    if computer_choice == 2:
        computer_choice_text = "Scissors"
        computer_choice_art = scissors

    print(f"You chose: {your_choice_text}")
    print(your_choice_art)
    print(f"Computer chose: {computer_choice_text}")
    print(computer_choice_art)
    print(who_wins)
