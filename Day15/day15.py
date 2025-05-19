
menu = {
    "espresso": {
        "ingredients" : {
            "water" : 50,
             "coffee": 18,
             "milk":0,
            },
        "cost" : 1.5,
    },
    "latte": {
        "ingredients" : {
             "water": 200,
            "milk" : 140,
             "coffee": 24,
            },
        "cost" : 2.5,
    },
    "cappuccino": {
        "ingredients" : {
             "water": 250,
            "milk" : 100,
             "coffee": 24,
            },
        "cost" : 3.0,
    }  
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True
def sufficient_resources(choice):
    if resources["water"] < menu[choice]["ingredients"]["water"]:
        print("Sorry, there is not enough water!!")
        return False
    
    if resources["coffee"] < menu[choice]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee!!")
        return False
        
    if resources["milk"] < menu[choice]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk!!")
        return False
    
    return True
def process_coins(quarter, dimes, nickles, pennies):
    total_money=quarter*0.5 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total_money
def is_money_enough(choice,moneycame):
    if menu[choice]["cost"] > moneycame:
        print("Sorry! That's not enough money. Money Refunded. ")
        return False
    return True   
    
coffee_choice=input("What  would you like? (Espresso/ Latte/ cappuccino: )").strip().lower()
if coffee_choice == "report":
    print(resources)
    coffee_choice=input("What  would you like? (Espresso/ Latte/ cappuccino: )").strip().lower()
    
sufficient_resources(coffee_choice)
print("Insert coins to get a drink")
quarter=float(input("Insert Quarters: $"))
dimes=float(input("Insert dimes: $"))
nickles=float(input("Insert nickles: $"))
pennies=float(input("Insert pennies: $"))
money_received=process_coins(quarter, dimes, nickles, pennies)
is_money_enough(coffee_choice,money_received)



