# MY ORIGINAL VERSION
# for number in range(1, 101):
#     # Check if the number is divisible by both 3 and 5
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     # Check if the number is divisible by 3
#     elif number % 3 == 0:
#         print("Fizz")
#     # Check if the number is divisible by 5
#     elif number % 5 == 0:
#         print("Buzz")
#     # If none of the above conditions are met, print the number itself
#     else:
#         print(number)

# CHATGPT'S OPTIMIZED VERSION
for number in range(1, 101):
    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    print(output or number)