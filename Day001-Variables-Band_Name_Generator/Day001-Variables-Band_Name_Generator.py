# Variables

# print() function - Print to the console
print("Hello, world!")

# Interactive Coding Exercise - Printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Add a new line
print("Hello, world!\nHello, world!\nHello, world!")

# Concatenation (operation of joining character strings end-to-end)
print("Hello" + " " + "Angela")

# input() function - Take input from the user and convert it into a string
input("A prompt for the user")
print("Hello " + input("What is your name?"))

# Interactive Coding Exercise - Printing
# Write a program that prints the number of characters in a user's name.
print(len(input("What is your name? ")))

# len() function - Return the length (the number of items) of an object

# Variables
name = input("What is your name? ")
length = len(name)
print(length)

# Interactive Coding Exercise - Variables
# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")
c = b
b = a
a = c
print("a: " + a)
print("b: " + b)

# Variable naming - best practice is using underscores
user_name = input("What is your name? ")

# Day 1 Project - Band Name Generator
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet name?\n")
print("Your band name could be " + city + " " + pet)
