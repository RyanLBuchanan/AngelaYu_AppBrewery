programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action doing something over and over again",
}

# # Retrieving items from a dictionary
# print(programming_dictionary["Bug"])
#
# # Adding new items to the dictionary
programming_dictionary["While Loop"] = "Perform an action while something remains true"
#
# print(programming_dictionary)
#
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in the dictionary
programming_dictionary["Bug"] = "Something went wrong"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
