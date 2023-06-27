# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
output = ""
for i in range(0, nr_letters):
    output += random.choice(letters)

for i in range(0, nr_symbols):
    output += random.choice(symbols)

for i in range(0, nr_numbers):
    output += random.choice(numbers)

print(f"Your easy password is: {output}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(
    "\nNow for the really random password to beat all the hackos!!!\n(ChatGPT helped a bit here ;)\n"
)

# Initialize an empty list to store the password components
password = []

# Generate random letters and append them to the password list
for _ in range(nr_letters):
    password.append(random.choice(letters))

# Generate random symbols and append them to the password list
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Generate random numbers and append them to the password list
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the password components to randomize their order
random.shuffle(password)

# Join the password components into a single string
output = ''.join(password)

print(f"Your difficult, really random password is: {output}")