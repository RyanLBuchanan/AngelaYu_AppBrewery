# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["fdhgjka"])
# except FileNotFoundError:
#     file = open("a_file.txt", "a")
#     file.write("Something that might cause an exception\n")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.  ")
# else:
#     content = file.read()
#     print(content)
# finally:
    # raise KeyError
    # raise TypeError("This is a message I made up.")


# height = float(input("height: "))
# weight = float(input("weight: "))
#
# if height > 3:
#     raise ValueError("No human is that tall, Holmes.")
#
# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]


# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(2)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0

print(f"Total likes: {total_likes}")
