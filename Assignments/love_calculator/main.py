# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Combine names and convert to lowercase
names = (name1 + name2).lower()

# Define lists of true characters and love characters
true_chars = ["t", "r", "u", "e"]
love_chars = ["l", "o", "v", "e"]

# Calculate scores for true characters and love characters
true_chars_score = sum(names.count(char) for char in true_chars)
love_chars_score = sum(names.count(char) for char in love_chars)

# Combine the scores into a love score
love_score = int(str(true_chars_score) + str(love_chars_score))

# Determine the outcome based on the love score
if 10 > love_score or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
