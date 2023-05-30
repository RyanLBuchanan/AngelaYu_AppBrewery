#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)
print(random_word)

hidden_word = ""
for letter in random_word:
    hidden_word += "_"

print(hidden_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guessed_letter = input("Guess a letter: ").lower()
print(guessed_letter)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in random_word:
    # print("Yes!  The letter you guessed is in the word.")
    if guessed_letter == letter:
        print("RIGHT!")
    else:
        print("WRONG!")

# Convert the string to a list
hidden_word_list = list(random_word)

index = hidden_word_list.index(guessed_letter)

# Replace the blank at the specified index with the guessed letter
hidden_word_list[index] = guessed_letter

# Convert the list back to a string
hidden_word = "".join(hidden_word_list)

print(hidden_word)



# if letter_guessed == letter in random_word:
#     for blank in blanks:
#         blanks = random_word[letter]
# else:
#     blanks += "_"
#
# print(blanks)