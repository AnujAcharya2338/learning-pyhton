
menu = {
    "espresso": {
        "ingredients" : {
            "water" : 50,
            "milk" : 0,
             "coffee": 18,
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
# def process_coins():
    

coffee_choice=input("What  would you like? (Espresso/ Latte/ cappuccino: )").strip().lower()
if coffee_choice == "report":
    print(resources)
sufficient_resources(coffee_choice)



