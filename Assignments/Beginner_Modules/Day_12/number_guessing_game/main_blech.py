import random
from art import logo
from colorama import Fore, Style

print(logo)

num_1 = 1
num_2 = 100

the_number = random.randint(num_1, num_2)

difficulty_level = input(f"Welcome to the Number Guessing Game\nI'm thinking of a number between {num_1} and "
                         f"{num_2}.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
    attempts = 10
else:
    attempts = 5

print(f"Psst, the number is: {the_number}.")

def guess():
    user_guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))

    if user_guess == the_number:
        return True
    elif user_guess > the_number:
        print("Too high.")
    else:
        print("Too low.")

    return False

while attempts != 0:
    if guess():
        print(f"{Fore.GREEN} \n***** You got it! The answer was {the_number}. *****\n {Style.RESET_ALL}")
        break
    attempts -= 1

    if attempts == 0:
        print(f"{Fore.RED} \n***** You've run out of guesses! You lose! Wamp waaaah! *****\n {Style.RESET_ALL}")

"""My original messy code below. The above was ChatGPT optimized version. Er . . .I was very close"""
# import random
#
# num_1 = 1
# num_2 = 100
#
# the_number = random.randint(1, 101)
#
# difficulty_level = input(f"Welcome to the Number Guessing Game\nI'm thinking of a number between {num_1} and "
#                          f"{num_2}.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
#
# print(f"Psst, the number is: {the_number}.")
#
# if difficulty_level == "easy":
#     attempts = 10
# else:
#     attempts = 5
#
# def guess(attempts):
#     user_guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
#
#     if user_guess == the_number:
#         print(f"You got it! The answer was {the_number}.")
#         exit()
#     elif user_guess > the_number and attempts > 0:
#         attempts -= 1
#         print(f"Too high.\nGuess again.")
#     elif user_guess < the_number and attempts > 0:
#         attempts -= 1
#         print(f"Too low.\nGuess again.")
#     else:
#         attempts = 0
#
#     return attempts
#
# while attempts > 0:
#     attempts = guess(attempts)
#
# print("You've run out of guesses! You lose! Wamp waaaah!")