
import random
def random_cards(first_card, second_card):
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    first_card=random.choice(cards)
    second_card=random.choice(cards)
    return first_card, second_card
    

playgame=input("Do you want to play a game og Blackjack? Type 'y' or 'n': ")
from art import logo
human_cards=random_cards(first_card="human",second_card="human2")
human_score="human1" + "human2"
        
    
    
