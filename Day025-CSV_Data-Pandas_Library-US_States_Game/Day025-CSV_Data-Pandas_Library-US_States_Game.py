# CSV Data and the Pandas Library

# CSV (Comma Separated Values) files represent data that fits into tables
import csv

with open("./Day025-CSV_Data-Pandas_Library-US_States_Game/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# The Pandas Library is a data analysis library
import pandas

data = pandas.read_csv("./Day025-CSV_Data-Pandas_Library-US_States_Game/weather_data.csv")
print(data)
print(data["temp"])
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(type(data["temp"]))  # <class 'pandas.core.series.Series'>

# DataFrame is the whole table
# Series is a column list

# Convert the DataFrame to a dictionary
data_dict = data.to_dict()
print(data_dict)

# Get data in a column
print(data["condition"])
print(data.condition)

# Find the min, max and average temperatures
print(data["temp"].min())
print(data["temp"].max())
print(data["temp"].mean())

# Get data in a row
print(data[data.day == "Monday"])

# Get data in the maximum temperature row
print(data[data.temp == data.temp.max()])

# Get the condition of a day
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Monday's temperature to Fahrenheit
monday = data[data.day == "Monday"]
temp_in_fahrenheit = monday.temp * 1.8 + 32
print(temp_in_fahrenheit)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

# Create a CSV file
data.to_csv("./Day025-CSV_Data-Pandas_Library-US_States_Game/new_data.csv")

# The Great Squirrel Census Data Analysis
# Count grey, red and black squirrels in Central Park in 2018
import pandas

data = pandas.read_csv("./Day025-CSV_Data-Pandas_Library-US_States_Game/squirrel_count.csv")
grey_squirrels_count = 0
red_squirrels_count = 0
black_squirrels_count = 0
for color in data["Primary Fur Color"]:
    if color == "Gray":
        grey_squirrels_count += 1
    elif color == "Cinnamon":
        red_squirrels_count += 1
    elif color == "Black":
        black_squirrels_count += 1

# Angela's solution
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dictionary = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

DataFrame = pandas.DataFrame(data_dictionary)
DataFrame.to_csv("./Day025-CSV_Data-Pandas_Library-US_States_Game/number_of_squirrels.csv")

# Day 25 Project - U.S. States Game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./Day025-CSV_Data-Pandas_Library-US_States_Game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("./Day025-CSV_Data-Pandas_Library-US_States_Game/50_states.csv")

score = 0
all_states = data.state.to_list()
correctly_guessed = []
answer_state = screen.textinput(title="Guess the State", prompt="What's a U.S. state's name?").title()
while score < 50:
    if answer_state == "Exit":
        for state in correctly_guessed:
            all_states.remove(state)
        missing_states = all_states
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./Day025-CSV_Data-Pandas_Library-US_States_Game/states_to_learn.csv")
        break
    for state in data["state"]:
        if answer_state == state:
            if answer_state not in correctly_guessed:
                t = turtle.Turtle()
                t.penup()
                t.hideturtle()
                state_data = data[data.state == answer_state]
                t.goto(int(state_data.x), int(state_data.y))
                t.write(answer_state)
                correctly_guessed.append(answer_state)
                score += 1
    if score < 50:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
