import random

# Get the names input from the user
names_string = input("Give me everybody's names, separated by a comma: ")

# Split the names string into a list of names
names = names_string.split(", ")

# Generate a random index to select a person to pay
num_to_pay = random.randint(0, len(names))

# Print length of names list
print(f"Length of names list: {len(names)}")

# Print the random number
print(f"Random number generated: {num_to_pay}")

# Get the person to pay based on the random index
person_to_pay = names[num_to_pay]

# Print the selected person who will buy the meal
print(f"{person_to_pay} is going to buy the meal today!")

# List of people at the table: Ryan, Chapel, Alita, Six, Seven