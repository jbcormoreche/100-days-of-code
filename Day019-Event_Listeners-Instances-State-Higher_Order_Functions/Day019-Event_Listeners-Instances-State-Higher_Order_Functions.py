# Event Listeners, Instances, State and Higher Order Functions

# Event Listeners
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()

# When you pass a function inside another function, you only pass the name without parentheses at the end.
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()


# Higher Order Functions are functions that contains other functions as a parameter or return a function as an output
def add(nl, n2):
    return nl + n2


def subtract(nl, n2):
    return nl - n2


def multiply(nl, n2):
    return nl * n2


def divide(nl, n2):
    return nl / n2


# Taking another function as an input and working with it inside the function
def calculator(nl, n2, func):
    return func(nl, n2)


result = calculator(2, 3, add)
print(result)

# Etch-a-Sketch
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_anticlockwise():
    tim.left(15)


def turn_clockwise():
    tim.right(15)


def clear_drawing():
    tim.reset()


screen.listen()

screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_anticlockwise)
screen.onkey(key="Right", fun=turn_clockwise)
screen.onkey(key="r", fun=clear_drawing)

screen.exitonclick()

# Object State and Instances
# Multiple objects with different attributes that can independently do different things have different states.

# Turtle Race
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

starting_position = -125
for turle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_position)
    starting_position += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
