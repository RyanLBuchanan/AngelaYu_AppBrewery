import random
from art import logo
from colorama import Fore, Style

print(logo)

num_1 = 1
num_2 = 100

# Generate a random number between num_1 and num_2
the_number = random.randint(num_1, num_2)

difficulty_level = input(
    f"Welcome to the Number Guessing Game\nI'm thinking of a number between {num_1} and {num_2}.\nChoose a difficulty. Type 'easy' or 'hard': "
).lower()

# Set the number of attempts based on the chosen difficulty level
if difficulty_level == "easy":
    attempts = 10
else:
    attempts = 5

def guess():
    # Prompt the user to make a guess
    user_guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))

    if user_guess == the_number:
        # The user guessed the correct number
        return True
    elif user_guess > the_number:
        # The user's guess is too high
        print("Too high.")
    else:
        # The user's guess is too low
        print("Too low.")

    # The user's guess was incorrect
    return False

# Main game loop
while attempts != 0:
    if guess():
        # The user guessed the correct number
        print(f"{Fore.GREEN} \n***** You got it! The answer was {the_number}. *****\n {Style.RESET_ALL}")
        break
    attempts -= 1

    if attempts == 0:
        # The user has run out of attempts
        print(f"{Fore.RED} \n***** You've run out of guesses! You lose! Wamp waaaah! *****\n {Style.RESET_ALL}")