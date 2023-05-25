# Print a welcome message to the rollercoaster program
# print("Welcome to the rollercoaster!")

# Input the height of the person in centimeters
# height = int(input("What is your height in cm? "))
#
# # Check if the person's height is equal to or greater than 120 cm
# if height >= 120:
#     print("You can ride the rollercoaster!")
#
#     # Input the age of the person
#     age = int(input("What is your age? "))
#
#     # Check the age to determine the ticket price
#     if age < 12:
#         print("Please pay $5.")
#     elif age >= 12 and age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you need to grow taller. :(")
#
# # Optimized ChatGPT
# print("Welcome to the rollercoaster!")
#
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#
#     ticket_price = 5 if age < 12 else 7 if age <= 18 else 12
#     print(f"Please pay ${ticket_price}.")
# else:
#     print("Sorry, you need to grow taller. :(")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you need to grow taller.:(")