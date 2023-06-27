# For loop to become a list comprehension
numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# List comprehension (generic)
"""new_list_comprehension = [new_item for item in list]"""

# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "T'Pol the Vulcanness"
# new_list = [letter + "\n" for letter in name]
# print(new_list)

"""
Python sequences:
list,
range,
string,
tuple
.. They have a specific order
list comprehension takes that sequence and goes through it in order
"""

# print([n * 2 for n in range(1, 5)])

"""Conditional List comprehension"""
# new_list_comprehension = [new_item for item in list if test]

sci_fi_girls = [
    "Trinity (The Matrix)",
    "Leeloo (The Fifth Element)",
    "Major Motoko Kusanagi (Ghost in the Shell)",
    "Seven of Nine (Star Trek: Voyager)",
    "Lara Croft (Tomb Raider)",
    "Sarah Connor (Terminator)",
    "Neytiri (Avatar)",
    "Aeon Flux (Aeon Flux)",
    "Pris (Blade Runner)",
    "Samantha (Her)"
]

star_trek_ladies = [
    "Seven",
    "T'Pol",
    "Jadzia",
    "Deanna",
    "Uhura",
    "Beverly",
    "Kira",
    "Nyota",
    "Ro"
]


short_names = [name for name in sci_fi_girls if len(name) < 10]

sexy_scifi_girls = {
    'Leeloo': 'The Fifth Element',
    'Pris': 'Blade Runner',
    'Trinity': 'The Matrix',
    'Cortana': 'Halo',
    'Seven of Nine': 'Star Trek: Voyager',
    'Lara Croft': 'Tomb Raider',
    'Major Motoko Kusanagi': 'Ghost in the Shell',
    'Sarah Connor': 'Terminator series',
    'Rachel': 'Blade Runner 2049',
    'Ava': 'Ex Machina'
}

sexy_star_trek_girls = {
    "Seven of Nine": "Star Trek: Voyager",
    "T'Pol": "Star Trek: Enterprise",
    "Deanna Troi": "Star Trek: The Next Generation",
    "Nyota Uhura": "Star Trek: The Original Series",
    "Ezri Dax": "Star Trek: Deep Space Nine",
    "B'Elanna Torres": "Star Trek: Voyager",
    "Jadzia Dax": "Star Trek: Deep Space Nine",
    "Christine Chapel": "Star Trek: The Original Series",
    "Ro Laren": "Star Trek: The Next Generation"
}

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [n**2 for n in numbers]
#
#
# #Write your code 👆 above:
#
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
# result = [n for n in numbers if n % 2 == 0]
#
#
# #Write your code 👆 above:
#
# print(result)
#
