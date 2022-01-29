# Day 29 Project - Password Manager GUI Application
import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered:\nEmail: {email}\nPassword: {password} \nIs it ok to save")

        if is_ok:
            with open("./Day029-Password_Manager_GUI_Application/data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, tk.END)
                password_input.delete(0, tk.END)


# UI setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = tk.Canvas(width=200, height=200)
mypass_img = tk.PhotoImage(file="./Day029-Password_Manager_GUI_Application/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = tk.Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = tk.Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "name@email.com")

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = tk.Entry(width=32)
password_input.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(width=49, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
