# NOT FINISHED


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

coffee_machine_resources = {"Water": [300, "ml"], "Milk": [200, "ml"], "Coffee": [100, "g"]}
#
print("Enter 'report' to get the stats for machine.\nEnter 'off' to turn off the machine.")
print("--------------------------------------------")


def choose_beverage(menu, collected_money, chosen_beverage):
    for beverage_name, beverage_info in menu.items():
        if beverage_name == chosen_beverage:
            cost = beverage_info["cost"]
            if cost <= collected_money:
                ingredients = beverage_info["ingredients"]
                for resource_name, value in ingredients.items():
                    if coffee_machine_resources[resource_name][0] < value:
                        print(f"Sorry, not enough {resource_name.lower()} to make {chosen_beverage}.")
                        return None
                for resource_name, value in ingredients.items():
                    coffee_machine_resources[resource_name][0] -= value
                print(f"Here is your {chosen_beverage} ☕️. Enjoy!")
                return beverage_name
            else:
                print(f"{chosen_beverage} is too expensive")
                print("Sorry, you can't afford any beverage")
                return None


def collect_money():
    coins = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
    print("Please insert coins.")
    sum = 0
    for coin, value in coins.items():
        coins[coin] = int(input(f"How many {coin}?: "))
    sum = coins["quarters"] * 25 + coins["dimes"] * 10 + coins["nickles"] * 5 + coins["pennies"]
    print(f"total money you inserted to the machine: {round((sum / 100), 2)}$")
    return round((sum / 100), 2)


#
#
while True:
    user_input = input("What would you like to take (espresso, latte, cappuccino): ")
    for beverage_name, beverage_info in MENU.items():
        if beverage_name == user_input:
            customer_money = collect_money()
            beverage = choose_beverage(MENU, customer_money, user_input)
            print(f"here is your {beverage}")

    if user_input == "report":
        for key, value in coffee_machine_resources.items():
            print(f"{key}: {value[0]}{value[1]}")
    if user_input == 'off':
        print("machine canceled the operation. Have a good day.")
        break

# print(collect_money())
#
# print(coffee_machine_resources)
