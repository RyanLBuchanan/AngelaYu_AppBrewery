# Import the logo from the art module
from art import logo

# Print the logo
print(logo)

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2

# Function to divide two numbers
def divide(n1, n2):
    return n1 / n2

# Dictionary to map operators to corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    # Prompt the user to enter the first number
    num_1 = int(input("What's the first number? "))

    # Display the available operators
    for operator, operation_function in operations.items():
        print(f"{operation_function.__name__.title()}: {operator}")

    # Variable to control the continuation of calculations
    continue_calculating = True

    # Main loop for continuous calculations
    while continue_calculating:
        # Prompt the user to select an operator
        operator = input("Pick an operation: ")

        # Prompt the user to enter the next number
        num_2 = int(input("What's the next number? "))

        # Retrieve the corresponding arithmetic operation function based on the selected operator
        operation_function = operations[operator]

        # Perform the calculation using the selected function
        answer = operation_function(num_1, num_2)

        # Display the calculation result
        print(f"Your calculation: {num_1} {operator} {num_2} = {answer}")

        # Prompt the user to continue or start a new calculation
        if input(f"Type \"y\" to continue calculating with {answer}, or type \"n\" to start a new calculation: ").lower() == "y":
            num_1 = answer
        else:
            continue_calculating = False
            calculator()

calculator()



    # # Check if the user wants to continue
    # while continue_input == "y":
    #     # Prompt the user to enter an operator
    #     operator = input("Pick another operation: ")
    #
    #     # Prompt the user to enter the next number
    #     num_2 = int(input("What's the next number? "))
    #
    #     # Retrieve the corresponding function for the selected operator
    #     operation_function = operations[operator]
    #
    #     # Perform the calculation using the selected operator and numbers
    #     second_answer = operation_function(first_answer, num_2)
    #
    #     # Display the calculation result
    #     print(f"Your calculation: {first_answer} {operator} {num_2} = {second_answer}")
    #
    #     continue_input = input(f"Type \"y\" to continue calculating with {second_answer}, or type \"n\" to start a new calculation: ").lower()
    #
    #     # Set the previous answer as the new first number for the next calculation
    #     first_answer = second_answer


