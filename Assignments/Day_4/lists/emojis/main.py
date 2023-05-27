import random

emojis = ["😀", "😂", "🥰", "😎", "🤩", "😊", "🥳", "😍", "🤗", "😁", "🤔", "😃", "😘", "🤣", "😇", "😉"]

# Set the desired number of emojis to select
num_emojis = 5

# Select a random group of emojis from the list
random_emojis = random.sample(emojis, num_emojis)

# Print the random group of emojis
print(random_emojis)

# https://getemoji.com/