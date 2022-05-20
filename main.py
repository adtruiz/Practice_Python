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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

resources_water = resources["water"]
resources_milk = resources["milk"]
resources_coffee = resources["coffee"]

request = input("What would you like? (espresso/latte/cappuccino): ").lower()

if request == "off":
    is_on = False
    print("Turning Off...")

elif request == "report":
    print(f"Water: {resources_water}ml")
    print(f"Milk: {resources_milk}ml")
    print(f"Coffee: {resources_coffee}g")
    print(f"Money: ${profit}")
    request_water = MENU[request]["ingredients"]["water"]
    request_milk = MENU[request]["ingredients"]["milk"]
    request_coffee = MENU[request]["ingredients"]["coffee"]

    resources_water -= request_water
    resources_milk -= request_milk
    resources_coffee -= request_coffee

elif request == "espresso" or request == "latte" or request == "cappuccino":
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    amount_entered = round((quarters + dimes + nickles + pennies), 2)
    request_amount = MENU[request]["cost"]
    change = round((quarters + dimes + nickles + pennies) - MENU[request]["cost"], 2)
    if amount_entered == request_amount:
        print(f"Here is your {request}. Enjoy!")
        print(f"Sorry that's not enough money. Money refunded.")
    elif request_amount < amount_entered:
        print(f"Here is ${change} in change.")
