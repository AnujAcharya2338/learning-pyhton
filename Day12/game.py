from art import logo
import random

print(logo)


def random_number():
    total_numbers = []
    for number in range(1, 101):
        total_numbers.append(number)
    return random.choice(total_numbers)

desired_number=random_number()
print(desired_number)

def high(guess):
    print("Too high.")
    print("Guess again.")
    choices(guess)

def low(guess):
    print("Too low.")
    print("Guess again.")
    choices(guess)

def won(guess):
    print(f"You got it! The answer was {desired_number}")

def difficulty(game_difficulty):
    print(f"You have {game_difficulty} attempts remaining to guess a number.")
    guess = input("Make a guess: ")
    choices(guess)
    
    
def choices(guess):
    if guess > desired_number:
        high(guess)
    elif guess < desired_number:
        low(guess)
    elif guess == desired_number:
        won(guess)

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    game_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if game_choice == "hard":
        difficulty(5)
    else:
        difficulty(10)
        
play_game()