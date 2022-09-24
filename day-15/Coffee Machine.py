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
    "money": 0,
}

def resource_check(x):
    if resources["water"] < MENU[x]["ingredients"]["water"]:
        print("Sorry there's not enough water")
    if resources["milk"] < MENU[x]["ingredients"]["milk"]:
        print("Sorry there's not enough milk")
    if resources["coffee"] < MENU[x]["ingredients"]["coffee"]:
        print("Sorry there's not enough coffee")
    else:
        return True

def coffee_check(x):
    change = round(money_calc() - MENU[x]["cost"], 2)
    if change < 0:
        resources["money"] = 0
        print("Sorry That's not enough money. Money refunded")
        return
    else:
        resources["water"] -= MENU[x]["ingredients"]["water"]
        resources["milk"] -= MENU[x]["ingredients"]["milk"]
        resources["coffee"] -= MENU[x]["ingredients"]["coffee"]
        resources["money"] -= change
        if change != 0:
            print(f"Here is ${change} in change")
        print(f"Here is your {x} ☕ Enjoy!")

def money_calc():
    quarter_total = 0.25 * quarters_in
    dime_total = 0.1 * dimes_in
    nickel_total = 0.05 * nickels_in
    penny_total = 0.01 * pennies_in
    totals = [quarter_total, dime_total, nickel_total, penny_total]
    money_in = sum(totals)
    resources["money"] += money_in
    return money_in

def start_coffee():
    global pennies_in
    global nickels_in
    global dimes_in
    global quarters_in
    global coffee
    coffee = str(input("What would you like? (espresso/latte/cappuccino): "))
    if coffee == "report":
        print(
            f"Water: {resources['water']}ml\n\
            Milk: {resources['milk']}ml\n\
            Coffee: {resources['coffee']}g\n\
            Money: ${resources['money']}")
    else:
        if resource_check(coffee) == True:
            quarters_in = int(input("How many Quarters?: "))
            dimes_in = int(input("How many Dimes?: "))
            nickels_in = int(input("How many Nickels?:"))
            pennies_in = int(input("How many Pennies?: "))
            money_calc()
            coffee_check(coffee)
    start_coffee()

start_coffee()
