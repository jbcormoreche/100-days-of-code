# Day 14 Project - Higher Lower Game
from higher_lower_data import data
from higher_lower_art import logo, vs
from random import randint

random_number1 = randint(0, 49)
random_number2 = randint(0, 49)

while random_number1 == random_number2:
    random_number2 = randint(0, 49)


# Choice A
def compare_A(random_number1):
    name_a = data[random_number1]["name"]
    description_a = data[random_number1]["description"]
    country_a = data[random_number1]["country"]
    follower_count_a = data[random_number1]["follower_count"]
    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    # print(f"Psst, number of followers = {follower_count_a}")
    return follower_count_a


# Choice B
def against_B(random_number2):
    name_b = data[random_number2]["name"]
    description_b = data[random_number2]["description"]
    country_b = data[random_number2]["country"]
    follower_count_b = data[random_number2]["follower_count"]
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
    # print(f"Psst, number of followers = {follower_count_b}")
    return follower_count_b


score = 0
you_are_right = True

while you_are_right is True:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    compare_A(random_number1)
    follower_count_a = data[random_number1]["follower_count"]
    print(vs)
    against_B(random_number2)
    follower_count_b = data[random_number2]["follower_count"]
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if follower_count_a > follower_count_b:
        right_answer = "a"
    else:
        right_answer = "b"
    print(right_answer)

    if answer != right_answer:
        you_are_right = False
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        score += 1
        random_number1 = random_number2
        random_number2 = randint(0, 49)
        while random_number1 == random_number2:
            random_number2 = randint(0, 49)
        print(f"You're right! Current score: {score}.")
