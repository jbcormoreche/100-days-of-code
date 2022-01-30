# Errors, Exceptions and JSON Data

# try:
# Something that might cause an exception

# except:
# Do this if there was an exception

# else:
# Do this if there were no exceptions

# finally:
# Do this no matter what happens

# Catch exceptions
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

# Raise exceptions
# Force a specified exception to occur
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

# Interactive Coding Exercise - IndexError Handling
# Prevent the program from crashing.
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# Interactive Coding Exercise - KeyError Handling
# Prevent the program from crashing.
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)

# Interactive Coding Exercise - Exception Handling in the NATO Alphabet Project
# Prevent the program from crashing if the user enters numbers or characters instead of letters.
import pandas

data = pandas.read_csv("./Day030-Errors-Exceptions-JSON_Data/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

is_valid = False
while is_valid is False:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        is_valid = True


# Angela's solution
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

# JSON (JavaScript Object Notation) is a lightweight format for storing and transporting data
# Write json.dump()
# Read json.load()
# Update/add new data json.update()

# Day 30 Project - Improved Password Manager GUI Application
import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# Password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    # String join() method - Return a string by joining all the elements of an iterable (list, string, tuple) separated by a string separator.
    password = "".join(password_list)
    password_input.insert(0, password)

    # Copy password to clipboard
    pyperclip.copy(password)


# Save password
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # Reading old data
            with open("./Day030-Errors-Exceptions-JSON_Data/data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # Creating json file and writing new data if file doesn't exist
            with open("./Day030-Errors-Exceptions-JSON_Data/data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            # Saving updated data
            with open("./Day030-Errors-Exceptions-JSON_Data/data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)


# Search password
def find_password():
    try:
        with open("./Day030-Errors-Exceptions-JSON_Data/data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        website = website_input.get()

        # Prefer conditional statements for things that happen frequently
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

        # Also possible with exceptions but it is best to use them for things that happen rarely of when you don't have an easy alternative
        # try:
        #     website = website_input.get()
        #     messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        # except KeyError:
        #     messagebox.showinfo(title="Error", message=f"There are no details for {website}.")


# UI setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = tk.Canvas(width=200, height=200)
mypass_img = tk.PhotoImage(file="./Day030-Errors-Exceptions-JSON_Data/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = tk.Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()
search_button = tk.Button(width=16, text="Search", command=find_password)
search_button.grid(column=2, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = tk.Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "name@email.com")

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = tk.Entry(width=33)
password_input.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(width=51, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
