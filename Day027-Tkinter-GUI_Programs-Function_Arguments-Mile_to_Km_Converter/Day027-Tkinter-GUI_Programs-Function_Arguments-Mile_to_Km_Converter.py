# Tkinter, GUI Programs and Function Arguments

# Tkinter and GUI Programs
import tkinter as tk


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label (text)
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Change or update a property of a component created
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry (text box)
input = tk.Entry(width=20)
input.pack()

# This line has to be at the end of the file.
window.mainloop()

# Layout Managers
# You need to specify a layout manager for elements to appear

# Pack: relative positioning, automatically places the widget based upon the space available in the window
# Place: precise/absolute positioning using x and y coordinates
# Grid: position the elements in rows and columns

# You can't use Pack and Grid at the same time (incompatibility)

# Second GUI
import tkinter as tk

window = tk.Tk()
window.title("My Second GUI Program")
window.minsize(width=500, height=300)
# Add padding around all 4 edges of GUI
window.config(padx=20, pady=20)

my_label = tk.Label(text="Label")
my_label.grid(column=0, row=0)
# Add padding around all 4 edges of GUI
my_label.config(padx=20, pady=20)

button1 = tk.Button(text="Button1")
button1.grid(column=1, row=1)

button2 = tk.Button(text="Button2")
button2.grid(column=2, row=0)

# Entry (text box)
input = tk.Entry(width=20)
input.grid(column=3, row=2)

window.mainloop()

# Keyword arguments with default values
# def my_function(a, b, c):
#     Do this with a
#     Then do this with b
#     Finally do this with c

# my_function(c=3, a=1, b=2)

# Arguments with default values
# def my_function(a=1, b=2, c=3):
#     Do this with a
#     Then do this with b
#     Finally do this with c

# my_function()

# Modify one input
# my_function(b=5)


# Unlimited positional arguments
# Define a function with a variable number of inputs (with no keyword)
def add(*args):
    print(args[0])  # Arguments are tuples

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 7, 8))


# Unlimited keyword arguments
# Define a function with a variable number of optional inputs (with keywords)
def calculate(n, **kwargs):
    # print(kwargs)  # Arguments are dictionaries
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # or
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# Create a class with lots of optional arguments
# Used to set options or to leave default values
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        # get() function returns None instead of a KeyError if the key doesn't exist in the dictionary
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)

# Day 27 Project - Mile to Km Converter
import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=40)
FONT = ("Arial", 18, "normal")


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=km)


miles_input = tk.Entry(width=8, font=FONT, justify="center")
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

result_label = tk.Label(text=" ", font=FONT)
result_label.grid(column=1, row=1)
result_label.config(padx=20, pady=20)

km_label = tk.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

button = tk.Button(text="Calculate", font=FONT, command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
