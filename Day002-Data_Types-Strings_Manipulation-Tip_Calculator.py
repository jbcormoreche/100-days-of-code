# Data Types

# Strings
print("Hello world!")

# Subscript: used to identify and access an element in a string or an array
# The index is the position of the element.
print("Hello"[0])

print("123" + "456")

# Integer
print(123 + 456)
print(123_456_789)  # easier to read for large numbers like 123,456,789

# Float
print(3.14159)

# Boolean
print(True)
print(False)

# type() function - Return the type of an object
print(type(123.25))

# Type conversion/casting
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = int(123.5)
print(type(a), ", a = ", a)

print(70 + float("100.5"))
print(str(70) + str(100))

# Interactive Coding Exercise - Data Types
# Write a program that adds the digits in a 2 digit number.
two_digit_number = input("Type a two digit number: ")
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
result = first_number + second_number
print(result)
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Mathematical Operations
3 + 5
7 + 4
3 * 2
6 / 3  # result is a float
2 ** 3

# Interactive Coding Exercise - BMI Calculator
# Write a program that calculates the Body Mass Index (BMI)
# from a user's weight and height.
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(float(weight) / float(height) ** 2)
print(bmi)

# Number manipulation

# round() function - Return number rounded to ndigits precision after the decimal point
# Round a number to 2 decimal digits
print(round(2.6666666666666, 2))
# If ndigits is omitted or is None, it returns the nearest integer to its input.
print(round(2.6666666666666))

# Floor division returns the largest possible integer
print(8 // 3)

score = 0
score += 1
print(score)

# f-Strings: improved way to format strings
print(f"Your score is {score}")

# Interactive Coding Exercise - Your Life in Weeks
age = input("What is your current age? ")
years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)

# String format() method - Perform string formatting operations
# Format a number to 2 decimal places
formatted_number = "{:.2f}".format(12.555555)
print(formatted_number)

# Day 2 Project - Tip Calculator
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
bill_per_person = round((total_bill + total_bill * percentage_tip / 100) / number_of_people, 2)
print(f"Each person should pay: ${bill_per_person}")
