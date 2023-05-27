# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

result = random.random() * 5

if result <= 2.5:
    print("Heads")
else:
    print("Tails")

#  ***** OR *****
# Optimized for brevity
print("Heads" if random.random() <= 2.5 else "Tails")

#  ***** OR *****
# How ChatGPT would write this given this prompt:
# "How would you write a heads tails generator using the Python random module?"
def flip_coin():
    result = random.choice(["Heads", "Tails"])
    return result

# Test the function
print(flip_coin())


