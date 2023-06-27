import random
from art import logo, vs
from game_data import data

"""Format account data into printable format"""
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take user guess and follower counts and returns if the user is correct"""
    # Use if statement to check if user is correct
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)

# Initialize score
score = 0

still_playing = True

account_b = random.choice(data)

# Make the game repeatable
while still_playing:
    # Generate random accounts from game data
    # Make account at position B become next account at position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Tyoe 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    print("\n" * 20)
    print(logo)
    # Give user feedback on their guess
    # Keep score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        still_playing = False
        print(f"Sorry, that's wrong. Final score: {score}")






