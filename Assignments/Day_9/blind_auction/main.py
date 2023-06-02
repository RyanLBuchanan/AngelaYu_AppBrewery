from art import logo

# Print the logo
print(logo)

# Create an empty dictionary to store the bids
bids = {}

# Flag to indicate if bidding is finished
bidding_finished = False

# Function to find the highest bidder from a bidding record
def find_highest_bidder(bidding_record):
    # Initialize the highest bid to 0
    highest_bid = 0

    # Loop through each bidder in the bidding record
    for bidder in bidding_record:
        # Get the bid amount for the current bidder
        bid_amount = bidding_record[bidder]

        # Check if the current bid amount is higher than the current highest bid
        if bid_amount > highest_bid:
            # Update the highest bid amount and winner
            highest_bid = bid_amount
            winner = bidder

    # Print the winner and the highest bid amount
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# Main bidding loop
while not bidding_finished:
    # Get the bidder's name
    name = input("What is your name? ")

    # Get the bid amount
    price = int(input("What is your bid? $"))

    # Add the bid to the dictionary
    bids[name] = price

    # Check if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")

    if should_continue == "no":
        # Bidding is finished, find the highest bidder
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clear the console for the next bidder
        print("\n" * 50)