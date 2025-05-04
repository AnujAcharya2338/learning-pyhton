import random
import os
from art import logo
def clear():
    os.system('cls' if os.name == 'nt' else 'ckear')
def random_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)>21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def commare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score>computer_score :
        return "You win"
    else:
        return "You Lose"
def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    is_game_over = False

    for _ in range(2):
        user_card.append(random_cards())
        computer_card.append(random_cards())

    while not is_game_over: 
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your card's: {user_card}, Current score: {user_score}  ")
        print(f"Computer's first card {computer_card[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal=input("Type 'y'o get another card or 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(random_cards())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score <17:
        computer_card.append(random_cards())
        computer_score = calculate_score(computer_card)  
    print(f"Your final hand:{user_card}, final score: {user_score}")
    print(f"Computer final hand:{computer_card}, final score: {computer_score}")
    print(commare(user_score,computer_score)) 


while input("DO you want to play a game of plackjack? type 'y' or 'no': ") == "y":
    clear()
    play_game()
    