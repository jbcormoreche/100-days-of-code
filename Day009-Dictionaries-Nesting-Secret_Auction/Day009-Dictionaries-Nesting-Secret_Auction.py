# Dictionaries and Nesting

# Dictionaries
# Used to store data values in key:value pairs
empty_dictionary = {}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Interactive Coding Exercise - Grading Program
# Write a program that converts students' scores from a database to grades.
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# Nesting

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    }
}

# Nesting a dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

# Interactive Coding Exercise - Dictionary in List
# Write a program that adds to a travel log.
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# Other solution
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {
        "country": country_visited,
        "visits": times_visited,
        "cities": cities_visited,
    }
    travel_log.append(new_country)


# Day 9 Project - Secret Auction
from secret_auction_art import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}
new_bidder = "yes"

while new_bidder == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders != "yes":
        new_bidder = "no"

winner_name = ""
highest_bid = 0
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner_name = bidder

print(f"The highest bidder is {winner_name} with a bid of ${highest_bid}.")
