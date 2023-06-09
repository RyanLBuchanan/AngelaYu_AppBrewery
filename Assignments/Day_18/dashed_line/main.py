# Import by module name
import random
import turtle
from turtle import Turtle, Screen

import heroes as heroes

"""OR"""
# import turtle as t
# !pip install heroes
import heroes

# from e import e
#
# start_e = e()
#
# # Your program code goes here
#  = Turtle()
#
# .shape("turtle")
# .color("DarkOliveGreen4")
#
# # for _ in range(4):
# #     my_the_turtle.forward(100)
# #     my_the_turtle.right(90)
#
# # List comprehension of the turtle square
# [.forward(100) or .right(90) for _ in range(4)]
#
#
# end_e = e()
# execution_e = end_e - start_e
#
# print(f"Program execution e: {execution_e} seconds")
#
#
"""Draw a square"""
#  = Turtle()
#
# .shape("turtle")
# .color("DarkOliveGreen4")
#
# # for _ in range(4):
#     my_the_turtle.forward(100)
#     my_the_turtle.right(90)
#
# # List comprehension of the turtle square
# # [.forward(100) or .right(90) for _ in range(4)]
#

# [print(f"{heroes.gen()}") for _ in range(10)]

# """Draw a dotted line"""
# tim = Turtle()
#
# # Set the pen color and size
# tim.color("black")
# tim.pensize(2)

# Set the pen style to "dot" and specify the dot size and spacing
# tim.pen(pencolor="black", pensize=2, pendown=True)
# tim.pendown()

# Draw the dotted line
# dot_size = 5  # Adjust the size of each dot
# dot_spacing = 10  # Adjust the spacing between dots
#
# # Octagon
# for _ in range(9):
#     for _ in range(10):
#         tim.forward(dot_size)
#         tim.penup()
#         tim.forward(dot_spacing)
#         tim.pendown()
#     tim.right(45)
#
# tim.penup()
# tim.forward(25)
# tim.right(45)
# tim.forward(dot_size/2)
# tim.penup()
# tim.forward(dot_spacing/2)
# tim.pendown()
# tim.penup()
# tim.forward(120)
#
# # Octagon inside an octagon
# for _ in range(8):
#     for _ in range(10):
#         tim.forward(dot_size * 0.5)
#         tim.penup()
#         tim.forward(dot_spacing * 0.5)
#         tim.pendown()
#     tim.right(45)
#
# # Hexagon
# # for _ in range(6):
# #     for _ in range(10):
# #         tim.forward(dot_size * 0.75)
# #         tim.penup()
# #         tim.forward(dot_spacing * 0.75)
# #         tim.pendown()
# #     tim.right(60)

