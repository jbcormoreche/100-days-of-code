# Flask Introduction, First Class Objects and Decorators

# Web Development with Flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return 'Bye'


if __name__ == '__main__':
    app.run()


# Functions are first-class objects and can be passed around as arguments (int, string, float...)
# Properties of first class functions:
# - A function is an instance of the Object type.
# - You can store the function in a variable.
# - You can pass the function as a parameter to another function.
# - You can return the function from a function.
# - You can store them in data structures such as hash tables, lists...


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 2, 3)
result = calculate(multiply, 2, 3)
print(result)


# Functions can be nested in other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()


# Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


inner_function = outer_function()
inner_function()


# Simple Python Decorator Functions
# A decorator takes in a function, adds some functionality and returns it.
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()  # run function twice
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")


# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()

# Interactive Coding Exercise - Create your own Python decorator
# Print out the speed it takes to run the fast_function() vs the slow_function()
import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        duration = end_time - start_time
        function_name = function.__name__
        print(f"The {function_name} took {duration} seconds.")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
