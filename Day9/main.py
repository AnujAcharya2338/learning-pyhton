import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'ckear')
    
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_fishished = False
while not bidding_fishished:
    name = input("What is your name?: ")
    price=int(input("What's your bid?: $"))
    bids[name] = price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_fishished = True
        highest_bidder(bids)
    elif should_continue =="yes":
        clear()
   
            
        
        
        
    
        
        
    
