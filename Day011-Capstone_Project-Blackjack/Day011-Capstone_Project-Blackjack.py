# Day 10 Capstone Project - Blackjack
import random
from blackjack_art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == 'y':
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    for i in range(2):
        random_card = deal_card()
        player_cards.append(random_card)
        player_score += random_card
        random_card = deal_card()
        computer_cards.append(random_card)
        computer_score += random_card
    print(logo)
    print(f"Your cards are {player_cards} and your current score is: {player_score}")
    print(f"Computer's first card is: {computer_cards[0]}")
    if player_score == 21:
        while computer_score < 17:
            for i in range(1):
                random_card = deal_card()
                computer_score += random_card
                computer_cards.append(random_card)
        if computer_score == 21:
            print("That's a draw, you both have Blackjack!")
        else:
            print(f"Computer's cards are: {computer_cards} and its final score is: {computer_score}")
            print("Blackjack, you win!")
    else:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        while player_score < 21 and another_card == "y":
            for i in range(1):
                random_card = deal_card()
                player_cards.append(random_card)
                player_score += random_card
                if player_score < 21:
                    print(f"Your cards are {player_cards} and your current score is: {player_score}")
                    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if player_score > 21 and 11 in player_cards:
            player_score -= 10
            print(f"Your cards are {player_cards} and your current score is: {player_score}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            while player_score < 21 and another_card == "y":
                for i in range(1):
                    random_card = deal_card()
                    player_cards.append(random_card)
                    player_score += random_card
                    if player_score < 21:
                        print(f"Your cards are {player_cards} and your current score is: {player_score}")
                        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if player_score == 21:
            while computer_score < 17:
                for i in range(1):
                    random_card = deal_card()
                    computer_cards.append(random_card)
                    computer_score += random_card
                if computer_score == 21:
                    print("That's a draw, you both have Blackjack!")
                else:
                    print(f"Your cards are {player_cards} and your current score is: {player_score}")
                    print("Blackjack, you win!")
                    print(f"Computer's cards are: {computer_cards} and its final score is: {computer_score}")

        elif player_score > 21:
            print(f"Your final hand is: {player_cards} and your final score is: {player_score}")
            while computer_score < 17:
                for i in range(1):
                    random_card = deal_card()
                    computer_cards.append(random_card)
                    computer_score += random_card
            print("You went over, you lose.")
        else:
            while computer_score < 17:
                for i in range(1):
                    random_card = deal_card()
                    computer_cards.append(random_card)
                    computer_score += random_card
            print(f"Your final hand is: {player_cards} and your final score is: {player_score}")
            print(f"Computer's final hand is {computer_cards} and its final score is: {computer_score}")
            if player_score > computer_score:
                print("You win!")
            elif player_score == computer_score:
                print("That's a draw.")
            elif player_score < computer_score and computer_score > 21:
                print("You win!")
            elif player_score < computer_score and computer_score < 22:
                print("You lose!")
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
