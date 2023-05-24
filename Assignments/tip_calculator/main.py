#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


# Print a welcome message to the tip calculator
print("Welcome to the tip calculator!")

# Input the total bill amount as a floating-point number
total_bill = float(input("What was the total bill? "))

# Input the tip percentage and convert it to a decimal
tip_percentage = int(input("What percentage tip would you like to give? ")) / 100

# Input the number of people to split the bill
num_people = int(input("How many people to split the bill? "))

# Calculate the amount each person should pay, including the tip
amount_per_person = (total_bill * (1 + tip_percentage)) / num_people

# Print the amount each person should pay, rounded to 2 decimal places
print(f"Each person should pay: ${round(amount_per_person, 2)}")
