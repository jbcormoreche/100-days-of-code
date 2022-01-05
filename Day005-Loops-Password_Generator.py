# Loops

# For Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# Interactive Coding Exercise - Average Height
# Write a program that calculates the average student height from a List of heights.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
number_of_students = 0
for student in student_heights:
    number_of_students += 1
average_height = total_height / number_of_students
print(round(average_height))

# Other solution with sum() and len() functions
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)

# Interactive Coding Exercise - High Score
# Write a program that calculates the highest score from a List of scores.
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

# For Loop and the range() function
# Print numbers between 0 and 10 and increment by 2.
for number in range(0, 11, 2):  # default step with only (0, 10) is 1
    print(number)

# Print the sum of the first 100 whole numbers.
total = 0
for number in range(1, 101):
    total += number
print(total)

# Interactive Coding Exercise - Adding Evens
# Write a program that calculates the sum of all the even numbers from 1 to 100.
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# Interactive Coding Exercise - FizzBuzz Job Interview Question
# Write a program that automatically prints the solution to the FizzBuzz game.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Day 5 Project - Password Generator

# Easy Level - Order not randomised
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
for number in range(0, nr_numbers):
    password += random.choice(numbers)

print(f"Your password is: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for letter in range(1, nr_letters + 1):
    password_list += random.choice(letters)
    # password_list.append(random.choice(letters))  works too
for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for number in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Random shuffle() method - Shuffle a list (reorganize the order of the list items)
random.shuffle(password_list)

shuffled_password = ""
for character in password_list:
    shuffled_password += character
print(f"Your password is: {shuffled_password}")
