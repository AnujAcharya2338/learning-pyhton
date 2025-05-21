
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
    total_money=quarter*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total_money
def is_money_enough(choice,moneycame,profit):
    if menu[choice]["cost"] > moneycame:
        print("Sorry! That's not enough money. Money Refunded. ")
        return False
    
    if menu[choice]["cost"] < moneycame:
            change_money= round(moneycame - menu[choice]["cost"], 2)
            print(f"Your change is: ${change_money} ")
            
    
    profit += menu[choice]["cost"]
    return profit

while is_on:
    coffee_choice=input("What  would you like? (Espresso/ Latte/ cappuccino: )").strip().lower()
    if coffee_choice == "off":
        is_on = False
        break
    if coffee_choice == "report":
        print(f"{resources} profit: {profit}")
        continue
    
    
    
    if not sufficient_resources(coffee_choice):
        continue
    print("Insert coins to get a drink")
    quarter=float(input("Insert Quarters: $"))
    dimes=float(input("Insert dimes: $"))
    nickles=float(input("Insert nickles: $"))
    pennies=float(input("Insert pennies: $"))
    money_received=process_coins(quarter, dimes, nickles, pennies)
    new_profit=is_money_enough(coffee_choice,money_received,profit)

    print(f"Here is your {coffee_choice}. Enjoy!")
    if new_profit :
        profit = new_profit
        resources["water"]=resources["water"]-menu[coffee_choice]["ingredients"]["water"]
        resources["coffee"]=resources["coffee"]-menu[coffee_choice]["ingredients"]["coffee"]
        resources["milk"]=resources["milk"]-menu[coffee_choice]["ingredients"]["milk"]
        
