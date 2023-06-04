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

# Display art
print(logo)

# Generate random accounts from game data
account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Against B: {format_data(account_b)}.")

# Ask user for a guess
guess = input("Who has more followers? Tyoe 'A' or 'B': ").lower()

# Check if user is correct
## Get follower count of each account
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

## Use if statement to check if user is correct

# Give user feedback on their guess

# Keep score

# Make the game repeatable

# Make account at position B become next account at position A

# Clear the screen between rounds



