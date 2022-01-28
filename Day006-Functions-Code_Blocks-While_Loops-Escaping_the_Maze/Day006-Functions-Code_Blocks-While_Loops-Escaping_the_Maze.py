# Functions, Code Blocks and While Loops

# Built-in functions
print("Hello")
num_char = len("Hello")
print(num_char)


# Defining and calling functions
def my_function():
    print("Hello")
    print("Bye")


my_function()


# Code blocks and indentation
def my_function2():
    sky = "clear"
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("Hello")


my_function2()

# While Loops - Iterate as long as the condition is true

# Reeborg's World challenges
# Hurdle 1
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)


# Hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():  # while at_goal() != True:  is possible too
    jump()


# Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_hurdle()
    elif front_is_clear():
        move()


# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()


while not at_goal():
    jump_hurdle()


# Day 6 Project - Escaping the Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
