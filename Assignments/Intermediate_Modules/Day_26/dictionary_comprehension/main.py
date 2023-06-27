import random
"""Dictionary Comprehension"""

# new_dict = {new_key:new_value for item in list}
# star_trek_ladies = { "lady": [
#     "Seven",
#     "T'Pol",
#     "Jadzia",
#     "Deanna",
#     "Uhura",
#     "Beverly",
#     "Kira",
#     "Nyota",
#     "Ro"
# ],
#     "hotness_score": [
#     9.5,
#     8.2,
#     8.6,
#     8.0,
#     8.7,
#     7.9,
#     8.3,
#     8.4,
#     7.7
#     ]
# }

# print(star_trek_ladies)

# hotness_scores = {name:random.randint(7, 10) for name in star_trek_ladies}
#
# # print(hotness_scores)
#
# top_hotness = {name:score for (name, score) in hotness_scores.items() if score > 8}
#
# print(top_hotness)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# sentence_word_list =  sentence.split()
# result = {word:len(word) for word in sentence.split()}
#
#
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:


# weather_f = {day:temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}
#
#
# # print(result)
# print(weather_f)

star_trek_ladies = { "lady": [
    "Seven",
    "T'Pol",
    "Jadzia",
    "Deanna",
    "Uhura",
    "Beverly",
    "Kira",
    "Nyota",
    "Ro"
],
    "hotness_score": [
    9.5,
    8.2,
    8.6,
    8.0,
    8.7,
    7.9,
    8.3,
    8.4,
    7.7
    ]
}

# for (key, value) in star_trek_ladies.items():
#     # print(f"Mistress {key} is hot such that your internal temperature rises {value} degrees.")
#     print(value)

import pandas as pd

st_ladies_df = pd.DataFrame(star_trek_ladies)
# print(st_ladies_df)

# Loop through dataframe
for (index, row) in st_ladies_df.iterrows():
    print(row.lady)