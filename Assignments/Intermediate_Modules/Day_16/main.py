# import another_module
# print(another_module.another_variable)

# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
#
# # Move Timmy forward by 100 paces
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

cyber_girls = PrettyTable()
cyber_girls.add_column("CyberGirls", ["Alita", "Major", "Six", "Seven"])
cyber_girls.add_column("Type", ["Battle Angel ", "Anime", "Toaster", "Borg"])
cyber_girls.add_column("Hotness", [8, 9, 10, 9])
# cyber_girls.align["CyberGirls"] = "l"
# cyber_girls.align["Hotness"] = "r"
cyber_girls.align = "l"

print(cyber_girls)



