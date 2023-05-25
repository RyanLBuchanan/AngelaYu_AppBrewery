# Print a welcome message to the rollercoaster program
print("Welcome to the rollercoaster!")

# Input the height of the person in centimeters
height = int(input("What is your height in cm? "))

# Check if the person's height is equal to or greater than 120 cm
if height >= 120:
    print("You can ride the rollercoaster!")

    # Input the age of the person
    age = int(input("What is your age? "))

    # Check the age to determine the ticket price
    if age < 12:
        print("Please pay $5.")
    elif age >= 12 and age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you need to grow taller. :(")

# Optimized ChatGPT
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    ticket_price = 5 if age < 12 else 7 if age <= 18 else 12
    print(f"Please pay ${ticket_price}.")
else:
    print("Sorry, you need to grow taller. :(")
