# Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Open the file containing the invited names list
invited_names_list = open("./Input/Names/invited_names.txt", "r")

# Read all the lines from the file and store them in a list
names_list = invited_names_list.readlines()

# Print the original list of names
print(names_list)

# Remove the newline character ('\n') from each name in the list
revised_names_list = [name.rstrip('\n') for name in names_list]

# Print the revised list of names without the newline character
# print(revised_names_list)

# Write letters replacing [name] with an actual name from the invited names list
with open("./Input/Letters/starting_letter.txt", "r") as original_letter:
    template_letter = original_letter.read()

    # Generate personalized letters for each name
    for name in revised_names_list:
        addressed_letter = template_letter.replace("[name]", name)

        # Save the personalized letter to a file
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as output_file:
            output_file.write(addressed_letter)




