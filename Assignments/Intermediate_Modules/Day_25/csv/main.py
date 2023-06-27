# with open("weather_data.csv", "r") as data:
#     data = data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# # average_temp = sum(temp_list) / len(temp_list)
# # print(round(average_temp, 2))
#
# average_temp = data["temp"].mean()
#
# print(f"Mean temperature: {round(average_temp, 2)}")
#
# max_temp = data["temp"].max()
#
# print(f"Max temperature: {max_temp}")
#
# min_temp = data["temp"].min()
#
# print(f"Min temperature: {data['temp'].min()}")
#
# # print(data["condition"])
# print(data.condition)

# How to get data in rows
# print(data[data.day == "Monday"])

# # Which day was the temperature
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# monday_temp_F = (monday.temp * 9/5) + 32
#
# print(monday_temp_F)

# Create a DataFrame from scratch
data_dict = {
    "Cybergirl": ["Alita", "Seven of Nine", "Chapel"],
    "Hotness": [8, 9, 9]
}

cybergirl_data = pd.DataFrame(data_dict)
print(cybergirl_data)

cybergirl_data.to_csv("cybergirl_data.csv")