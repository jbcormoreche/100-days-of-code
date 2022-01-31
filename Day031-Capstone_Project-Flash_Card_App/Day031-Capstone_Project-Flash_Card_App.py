# Day 31 Capstone Project - Flash Card App
import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./Day031-Capstone_Project-Flash_Card_App/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./Day031-Capstone_Project-Flash_Card_App/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    next_card.current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=next_card.current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=next_card.current_card["English"], fill="white")


def is_known():
    to_learn.remove(next_card.current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./Day031-Capstone_Project-Flash_Card_App/data/words_to_learn.csv", index=False)
    next_card()


# UI Setup
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="./Day031-Capstone_Project-Flash_Card_App/images/card_front.png")
card_back_image = tk.PhotoImage(file="./Day031-Capstone_Project-Flash_Card_App/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

wrong_image = tk.PhotoImage(file="./Day031-Capstone_Project-Flash_Card_App/images/wrong.png")
red_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_card)
red_button.grid(column=0, row=1)

right_image = tk.PhotoImage(file="./Day031-Capstone_Project-Flash_Card_App/images/right.png")
green_button = tk.Button(image=right_image, highlightthickness=0, command=is_known)
green_button.grid(column=1, row=1)

next_card()

window.mainloop()
