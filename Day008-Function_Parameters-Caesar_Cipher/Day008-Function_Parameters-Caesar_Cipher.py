# Function Parameters

# Functions with inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")


greet_with_name("George")

# Arguments and parameters
# A function has parameters and takes arguments
# name is the parameter (name of the data used inside the function)
# "George" is the argument, the actual value of the data being passed in (used when calling the function)

# Functions with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")


# Functions with positional arguments (arguments that can be called by their position)
greet_with("Sarah", "Manchester")

# Functions with keyword arguments (arguments that can be called by their name)
greet_with(location="Manchester", name="Sarah")

# Interactive Coding Exercise - Paint Area Calculator
import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil(height * width / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

# Interactive Coding Exercise - Prime Number Checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if (number % i == 0):
            is_prime = False
    if is_prime:  # same as if is_prime is True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

# Day 8 Project - Caesar Cipher
# Encode and decode messages by shifting each letter a certain number of places down the alphabet
from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(choice, start_text, shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            if choice == "encode":
                new_position = alphabet.index(char) + shift_amount
                if new_position > 25:
                    new_position %= 26
            elif choice == "decode":
                new_position = alphabet.index(char) - shift_amount
                if new_position < -25:
                    new_position %= 26
                elif new_position < 0:
                    new_position += 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    if choice == "encode":
        print(f"The encoded message is {end_text}")

    if choice == "decode":
        print(f"The decoded message is {end_text}")


go = "yes"
print(logo)

while go == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
        go = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    else:
        print("You didn't write one of the choices correctly.")

print("Goodbye")
