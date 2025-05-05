from art import logo
import random

print(logo)


def random_number():
    total_numbers = []
    for number in range(1, 101):
        total_numbers.append(number)
    return random.choice(total_numbers)


def high(attempts):
    print("Too high.")
    print("Guess again.")
    return attempts-1


def low(attempts):
    print("Too low.")
    print("Guess again.")
    return attempts-1


def won():
    return print(f"You got it! The answer was {desired_number}")


def choices(guess_number, attempts):
    if guess_number > desired_number:
        return high(attempts)
    elif guess_number < desired_number:
        return low(attempts)
    else:
        won()
        return -1

def guess(game_difficulty):
    attempts = game_difficulty
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess a number.")
        guess_number = int(input("Make a guess: "))
        result=choices(guess_number, attempts)
        if result == -1:
            return
        else:
            attempts = result
    print(f"You have run out of guesses.The number was {desired_number}.")    


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    game_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if game_choice == "hard":
        guess(5)
    else:
        guess(10)


desired_number = random_number()
print(desired_number)

play_game()
