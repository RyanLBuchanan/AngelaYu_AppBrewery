from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#                 '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
#                 '-', '_', '+', '=', '[', ']', '{', '}', '|', ';',
#                 ':', ',', '.', '/', '?', '<', '>', '~',
#                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                 'u', 'v', 'w', 'x', 'y', 'z']

# Creating a list of numbers from 0 to 9
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Creating a list of symbols
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '?', '<', '>', '~']

print(logo)

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        # elif char in numbers:
        #     position = numbers.index(char)
        #     new_position = (position + shift_amount) % len(numbers)
        #     end_text += numbers[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}.\n")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))

    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    else:
       print("That is an unrecognized input!")
       exit()

    # shift = shift % 26 # Angela's solution for her alphabet -> we divide the result for new position by len(alphabet)
                         # in line 31


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(f"Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if result == "no":
        should_continue = False
        print("Thank you for your service.\nHappy tradecraft!")





################################ PREVIOUS SEPARATE FUNCTIONS
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = (position + shift) # % len(alphabet)
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
# # Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount):
#     original_text = ""
#   # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in
#     # the alphabet by the shift amount and print the decrypted text.
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = (position - shift_amount)
#         new_letter = alphabet[new_position]
#         original_text += new_letter
#
#     print(f"The decoded text is {original_text}")



# Check if the user wanted to encrypt or decrypt the message by checking the
# 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# if direction == "encode":
#     # Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)



################################
# CHATGPT CODE
# # Create an array to hold the indexes of the input characters
#     output_text_list = []
#
#     for char in text:
#         # output_text_list += output_text_list.append(alphabet[i])
#         if char in alphabet:
#             # Find the index of the character in alphabet
#             index = alphabet.index(char)
#             # Shift the index by the shift value
#             shifted_index = (index + shift) % len(alphabet)
#             # Get the shifted letter from the alphabet
#             shifted_char = alphabet[shifted_index]
#             # Append the shifted character to the output list
#             output_text_list.append(shifted_char)
#
#     output_text = "".join(output_text_list)
#     print(f"The encoded text is {output_text}")