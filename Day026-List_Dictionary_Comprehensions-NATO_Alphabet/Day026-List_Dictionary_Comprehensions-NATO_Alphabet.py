# List and Dictionary Comprehensions

# List Comprehension
# Shorter syntax for creating a new list from an existing list
# new_list = [new_item for item in list]

# Using a for loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# Using list comprehension with a list
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

# Using list comprehension with a string
name = "Angela"
letters_list = [letter for letter in name]

# Lists, strings, tuples and range are sequences because they have a certain order
new_range = [n * 2 for n in range(1, 5)]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) > 5]
capitalized_long_names = [name.upper() for name in names if len(name) < 5]

# Interactive Coding Exercise - Squaring Numbers
# Create a new list that contains every number in the list numbers but each number should be squared.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# Interactive Coding Exercise - Filtering Even Numbers
# Create a new list that contains the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)

# Interactive Coding Exercise - Data Overlap
# Create a list called which contains the numbers that are common in both files.
with open("./Day026-List_Dictionary_Comprehensions-NATO_Alphabet/file1.txt") as file1:
    num1 = file1.readlines()
numbers1 = [int(num.strip("\n")) for num in num1]

with open("./Day026-List_Dictionary_Comprehensions-NATO_Alphabet/file2.txt") as file2:
    num2 = file2.readlines()
numbers2 = [int(num.strip("\n")) for num in num2]

result = [common for common in numbers1 if common in numbers2]
print(result)

# Dictionary Comprehension
# Shorter syntax for creating a new dictionary from an existing dictionary
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new value for (key,value) in dict.items()}
# new_dict = {new_key:new value for (key, value) in dict.items() if test}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# Interactive Coding Exercise - Dictionary Comprehension 1
# Create a dictionary that takes each word in a given sentence and calculates the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# Interactive Coding Exercise - Dictionary Comprehension 2
# Create a dictionary that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# Iterate over a Pandas DataFrame
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Loop through a dictionary
for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)

# Day 26 Project - NATO Alphabet
import pandas

data = pandas.read_csv("./Day026-List_Dictionary_Comprehensions-NATO_Alphabet/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
