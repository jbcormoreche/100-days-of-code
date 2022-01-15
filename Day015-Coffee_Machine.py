# Day 15 Project - Coffee Machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


customer_choice = input("What would you like? (espresso/latte/cappuccino): ")
while customer_choice != "off":
    enough_ressources = True
    if customer_choice == "report":
        report()
        customer_choice = input("What would you like? (espresso/latte/cappuccino): ")
    else:
        missing_ingredients = []
        for ingredient in MENU[customer_choice]["ingredients"]:
            if resources[ingredient] < MENU[customer_choice]["ingredients"][ingredient]:
                enough_ressources = False
                missing_ingredients.append(ingredient)
        if enough_ressources is False:
            if len(missing_ingredients) == 1:
                print(f"Sorry there is not enough {missing_ingredients[0]}.")
            elif len(missing_ingredients) == 2:
                print(f"Sorry there is not enough {missing_ingredients[0]} and {missing_ingredients[1]}.")
            elif len(missing_ingredients) == 3:
                print(f"Sorry there is not enough {missing_ingredients[0]}, {missing_ingredients[1]} and {missing_ingredients[2]}.")
        if enough_ressources is True:
            customer_choice_cost = MENU[customer_choice]["cost"]
            customer_choice_ingredients = MENU[customer_choice]["ingredients"]
            print(f"The price is: ${customer_choice_cost}")
            print("Please insert coins.")
            customer_quarters = int(input("How many quarters ($0.25)?: "))
            customer_dimes = int(input("How many dimes ($0.10)?: "))
            customer_nickles = int(input("How many nickles ($0.05)?: "))
            customer_pennies = int(input("How many pennies ($0.01)?: "))
            customer_paid = customer_quarters * 0.25 + customer_dimes * 0.1 + customer_nickles * 0.05 + customer_pennies * 0.01
            if customer_paid < customer_choice_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                for ingredient in customer_choice_ingredients:
                    resources[ingredient] -= customer_choice_ingredients[ingredient]
                if customer_paid == customer_choice_cost:
                    print(f"You paid: ${customer_paid}")
                    resources["money"] += customer_paid
                    print(f"Here is your {customer_choice}. Enjoy!")
                else:
                    print(f"You paid: ${customer_paid}")
                    change = round((customer_paid - customer_choice_cost), 2)
                    resources["money"] += customer_choice_cost
                    print(f"Here is your change: ${change}")
                    print(f"Here is your {customer_choice}. Enjoy!")
        customer_choice = input("What would you like? (espresso/latte/cappuccino): ")
