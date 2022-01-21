# Class Inheritance and List Slicing

# Class Inheritance
# Define a class that inherits all the methods and properties from another class
# Reuse code and add more features to a class without modifying it
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# Slicing lists
# Used to access a range of elements in a list
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5])  # returns ['c', 'd', 'e']

# Slicing from the start of a list to a position
print(piano_keys[:5])  # returns ['a', 'b', 'c', 'd', 'e']

# Slicing from a position to the end of a list
print(piano_keys[2:])  # returns ['c', 'd', 'e', 'f', 'g']

# Slicing between 2 positions with an increment
print(piano_keys[2:5:2])  # returns ['c', 'e']

# Slicing a list with an increment
print(piano_keys[::2])  # returns ['a', 'c', 'e', 'g']

# Reverse a list
print(piano_keys[::-1])  # returns ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Slicing tuples
# Used to access a range of elements in a tuple
piano_keys = ("do", "re", "mi", "fa", "sol", "la", "si")
print(piano_keys[2:5])  # returns ('mi', 'fa', 'sol')

# Day 21 Project - Snake Game Part 2
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
screen = Screen()
food = Food()
scoreboard = Scoreboard()
tim = Turtle()

screen.setup(width=610, height=640)
screen.bgcolor("black")
screen.title("Snake Game")
tim.hideturtle()
tim.speed(5)
tim.penup()
tim.color("white")
tim.goto(-280, -290)
tim.pendown()
tim.forward(560)
tim.left(90)
tim.forward(580)
tim.left(90)
tim.forward(560)
tim.left(90)
tim.forward(580)
tim.penup()
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
