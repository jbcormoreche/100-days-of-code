# Graphical User Interface and Tuples
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# Draw a square
for _ in range(4):
    tim.forward(100)
    tim.left(90)

# Draw a dashed line
for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.exitonclick()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for sides in range(3, 11):
    tim.color(random.choice(colors))
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)

screen = Screen()
screen.exitonclick()

# Generate a random walk
from turtle import Turtle, Screen
import random

tim = Turtle()

directions = [0, 90, 180, 270]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(12)
tim.speed(0)
for _ in range(300):
    tim.forward(25)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

# Tuples are lists that cannot be changed
my_tuple = (1, 3, 8)

# Convert a tuple into a list
my_tuple = list(my_tuple)
my_tuple += [11, 13, 18]
print(my_tuple)

# Generate a random walk with random RGB colors
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
tim.pensize(12)
tim.speed(0)
for _ in range(300):
    tim.forward(25)
    tim.color(random_color())
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

# Generate a spirograph
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(360):
    if i % 1 == 0:
        tim.setheading(i)
        tim.color(random_color())
        tim.circle(100)

screen = t.Screen()
screen.exitonclick()

# Day 18 Project - Hirst Painting
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# Colors extracted from an actual Hirst painting using the cologram.py library
colors = [(228, 228, 226), (199, 175, 117), (125, 36, 24), (169, 104, 56), (187, 158, 51), (207, 220, 211), (6, 56, 83), (109, 67, 85), (40, 35, 34), (87, 141, 57), (20, 122, 175), (110, 160, 175), (75, 39, 48), (9, 67, 47), (64, 153, 137), (183, 98, 80), (133, 40, 43), (179, 201, 187), (208, 200, 125), (150, 176, 164), (178, 167, 170), (95, 141, 154), (31, 78, 59)]

# Initialize position to center painting
tim.penup()
tim.hideturtle()
tim.setheading(180)
tim.forward(200)
tim.setheading(270)
tim.forward(200)
tim.setheading(0)


def draw_row():
    for i in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(40)


y = -200
for i in range(10):
    tim.setposition(-200, y)
    draw_row()
    y += 40

screen = t.Screen()
screen.exitonclick()
