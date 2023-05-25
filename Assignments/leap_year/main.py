# Set a variable to True to enter the while loop
continue_program = True

# While loop to keep the program running as long as the user wants to continue
while continue_program:
    # Get the year from the user
    year = int(input("Enter a year: "))

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, it is not a leap year unless it is also divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                # If the year is divisible by 400, it is a leap year
                print(year, "is a leap year.")
            else:
                # If the year is not divisible by 400, it is not a leap year
                print(year, "is not a leap year.")
        else:
            # If the year is not divisible by 100, but it is divisible by 4, it is a leap year
            print(year, "is a leap year.")
    else:
        # If the year is not divisible by 4, it is not a leap year
        print(year, " is not a leap year.")

    # Ask the user if they want to continue
    answer = input("Do you want to check another year? (yes/no) ")
    if answer.lower() != "yes":
        # If the answer is not "yes", set the continue_program variable to False to exit the while loop
        continue_program = False