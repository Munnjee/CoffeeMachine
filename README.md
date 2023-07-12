# Coffee Machine

This is a simple coffee machine program written in Python. It allows users to choose from a menu of drinks (espresso, latte, or cappuccino), insert coins to pay for the chosen drink, and dispenses the selected drink if there are sufficient ingredients and the payment is enough. The program keeps track of the available resources (water, milk, coffee) and the total cash received.

## Requirements

- Python 3.x

## Usage

1. Run the program using `python main.py`.
2. Follow the on-screen instructions to select a drink, insert coins, and receive the drink.

## Files

The program consists of two files:

- `main.py` - Contains the main code for the coffee machine program.
- `art.py` - Contains the ASCII art used for visual elements in the program.

## Menu

The menu consists of the following drinks:

1. Espresso - A strong coffee brewed by forcing hot water under pressure through finely ground coffee beans.
2. Latte - A coffee drink made with espresso and steamed milk.
3. Cappuccino - A coffee drink made with espresso, steamed milk, and a frothy milk foam topping.

Each drink has a specific set of ingredients and a cost associated with it.

## Resources

The coffee machine keeps track of the following resources:

- Water - The amount of water available in milliliters (ml).
- Milk - The amount of milk available in milliliters (ml).
- Coffee - The amount of coffee available in grams (g).

The resources are used to make the selected drink. If there are not enough resources to make a drink, the program will display an error message.

## Payment

The program accepts the following coins for payment:

- Toonies - $2 coins
- Loonies - $1 coins
- Quarters - $0.25 coins
- Dimes - $0.10 coins
- Nickels - $0.05 coins

The user is prompted to insert the required number of each coin. The total tender received is calculated based on the coins inserted. If the payment is sufficient, the program will dispense the selected drink and provide any change due. Otherwise, an error message will be displayed.

## Reporting

To view the current status of the coffee machine, you can enter the command "report". This will display the current amount of each resource (water, milk, coffee) and the total cash received so far.

## Turning Off

To turn off the coffee machine, enter the command "off". This will exit the program.

## Art

The program uses ASCII art to display a coffee cup and other visual elements. These visual elements are defined in the `art.py` file and imported into the `main.py` file.

Enjoy your coffee!
