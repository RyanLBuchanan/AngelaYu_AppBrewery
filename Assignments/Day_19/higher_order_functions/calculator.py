def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Cannot divide by zero.")

# Higher order function "calculator
def calculator(num1, num2, func):
    return func(num1, num2)

result = calculator(2, 3, multiply)
print(result)
