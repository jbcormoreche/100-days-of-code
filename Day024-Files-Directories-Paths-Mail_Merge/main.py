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
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
