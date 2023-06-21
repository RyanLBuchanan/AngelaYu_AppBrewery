# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew stuff!")

with open("../../", mode="w") as file:
    file.write("\nSpecial stuff!")

# import os
#
# file_path = 'C:/Users/vreed/Desktop/Python/Udemy/AngelaYu/AngelaYu_AppBrewery/Assignments/Day_24/my_files/my_file.txt'
#
# if os.access(file_path, os.W_OK):
#     print(file_path)
# else:
#     print("no worky stuff")