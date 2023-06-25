# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Orange"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

"""
try:
    Something that might cause an exception
except:
    Do this if there was an exception
else:
    Do this if there were no exceptions
finally:
    Do this no matter what happens
"""

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["fdhgjka"])
except FileNotFoundError:
    file = open("a_file.txt", "a")
    file.write("Something that might cause an exception\n")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.  ")