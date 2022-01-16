# Object Oriented Programming (OOP)

# Procedural Programming (top down approach)
# Procedures consist of a series of computational steps to be carried out
# During a program’s execution, any given procedure might be called at any point, including by other procedures or itself

# Object Oriented Programming (bottom up approach)
# Split a larger task into smaller pieces that can be worked on separately
# Each piece becomes reusable

# Classes are blueprints for creating objects and provide a means of bundling data and functionality
# PascalCase is used for classes to differentiate from variables and functions

# An object is a collection of data(variables) and methods(functions)

# Attributes are variables associated with an object (have things)
# Methods are functions associated with an object (do things)

# Import a class/classes
from turtle import Turtle, Screen

# Create a new object
timmy = Turtle()
print(timmy)

# Call methods associated with objects
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

my_screen = Screen()

# Tap into an object attribute
print(my_screen.canvheight)
my_screen.exitonclick()

# Packages are a bunch of code made by other people for a purpose
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# Change the object attribute
table.align = "l"
print(table)

# Day 16 Project - Coffee Machine in OOP
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
