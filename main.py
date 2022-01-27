import os
balance = 0
is_Off = False
money = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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


def clearConsole():
    command = 'clear'
    if os.name in ['dos', 'nt']:
        command = 'cls'
    os.system(command)


def check_Resources(coffee, resources):
    if coffee['water'] > resources['water']:
        print("Sorry there is not enough water")
        return False
    elif coffee['milk'] > resources['milk']:
        print("Sorry there is not enough milk")
        return False
    elif coffee['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee powder")
        return False
    else:
        return True


def deduct_Resources(coffee, resources):
    resources['water'] -= coffee['water']
    resources['milk'] -= coffee['milk']
    resources['coffee'] -= coffee['coffee']
    return resources


while not is_Off:
    order = input("What would you like. (espresso\latte\cappuccino): ")
    if order in ['espresso', 'latte', 'cappuccino']:
        total = 0
        coffee = MENU[order]
        if check_Resources(coffee["ingredients"], resources):
            print("Please insert coins")
            quarters = int(input("How many quarters: ")) * 0.25
            dimes = int(input("How many dimes: ")) * 0.10
            nickels = int(input("How many nickels: ")) * 0.05
            pennis = int(input("How many pennis: ")) * 0.01
            total = quarters + dimes + nickels + pennis + balance
            if total >= coffee["cost"]:
                balance = total - coffee['cost']
                balance = round(balance, 2)
                print(f"Here is your {order} ☕ Enjoy!")
                if balance > 0:
                    print(f"Here is your balance ${balance}")
                resources = deduct_Resources(coffee["ingredients"], resources)
                money += coffee['cost']
            else:
                print(f"Sorry that's not enough money.Money refunded ${total}")
    elif order == 'off':
        is_Off = True
    elif order == 'report':
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    else:
        print("Invalid input")

