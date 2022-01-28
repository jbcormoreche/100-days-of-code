# Tkinter and Dynamic Typing

# Dynamic typing
# Python allows changing the data type of a variable by assigning it to a different type of value.
# The type of the value is determined during run-time.

# Day 28 Project - Pomodoro GUI Application
import tkinter as tk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# Timer reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# Timer mechanism
def start_timer():
    global reps
    global timer_label
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    Long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(Long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# Countdown mechanism
def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# UI setup
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# The Canvas widget is used to layer things on top of each other
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="./Day028-Tkinter-Dynamic_Typing-Pomodoro_GUI_Application/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = tk.Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
