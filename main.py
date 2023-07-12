import os
from art import logo, coffee, closed

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
}

till = 0


def parse_data(input_data):
    water = input_data["water"]
    milk = input_data["milk"]
    coffee = input_data["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g"


def sufficient_ingredient(order_item):
    """Checks resources dictionary and returns True if order can be made, False if not enough ingredients"""
    for ingredient in order_item:
        if order_item[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
        return True


def total_cash():
    """Returns total tender received from coins inserted"""
    print("Please insert coins.")
    total_paid = float(input("How many toonies?: ")) * 2
    total_paid += float(input("How many loonies?: "))
    total_paid += float(input("How many quarters?: ")) * 0.25
    total_paid += float(input("How many dimes?: ")) * 0.1
    total_paid += float(input("How many nickels: ")) * 0.05
    return total_paid


def sufficient_payment(money_paid, price):
    """Returns True if total tender received is more than price of order, False if not enough payment"""
    if money_paid >= price:
        change = money_paid - price
        print(f"Here is ${change:.2f} in change.")
        global till
        till += price
        return True
    else:
        print("Sorry, that's not enough money. Here is your payment back.")
        return False


def make_coffee(order_item, order_ingredients):
    """Deduct ingredients used to make order from resources"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(coffee)
    print(f"Here is your {order_item}. Enjoy!")


machine_on = True

while machine_on:
    print(logo)
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        machine_on = False
    elif order == "report":
        print(parse_data(resources))
        print(f"Money: ${till:.2f}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        drink = MENU[order]
        print(f"That will be ${drink['cost']:.2f}.")
        if sufficient_ingredient(drink["ingredients"]):
            payment = total_cash()
            if sufficient_payment(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
    else:
        print(f"{order} is not on the menu, Please try again!")

    if machine_on:
        input("Press Enter to continue...\n")
    os.system('cls' if os.name == 'nt' else 'clear')

print(closed)
print("Machine turned off. Good bye!")



