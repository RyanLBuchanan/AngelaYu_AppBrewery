# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_to_pay = random.randint(0, len(names))

person_to_pay = names[num_to_pay]

print(f"{person_to_pay} is going to buy the meal today!")

# List for people at table: Ryan, Chapel, Alita, Six, Seven