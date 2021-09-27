from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

print(logo)

money_collected = 0


def enough_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.1
    nickels = float(input("How many nickels? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def check_money(money_received, coffee_cost):
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        global money_collected
        money_collected += coffee_cost
        return True
    else:
        print("Sorry not enough money. Money refunded.")
        return False


def prepare_coffee(coffee_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name}☕. Enjoy!")


make_coffee = True

while make_coffee:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        make_coffee = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_collected}")
    else:
        selected_coffee = MENU[user_choice]
        if enough_resources(selected_coffee["ingredients"]):
            money_inserted = insert_coins()
            if check_money(money_received=money_inserted, coffee_cost=selected_coffee["cost"]):
                prepare_coffee(coffee_name=user_choice, ingredients=selected_coffee["ingredients"])










