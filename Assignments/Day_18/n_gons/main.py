import random
import turtle
from turtle import Turtle, Screen

""" N-gons in range(3 - 10)"""
tim = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


# Function to generate random color values
def get_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


for shape_side_n in range(3, 11):
    tim.color(get_random_color())
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()



"""MY BLECHY CODE BELOW!!!"""
# # Function to generate random color values
# def get_random_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     return (r, g, b)
#
#
# # Reset heading and change color
# # def reset_tim(counter):
#
#
#
# range_counter = 4
#
# # Triangle
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / 3)
#
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# # Square
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / range_counter)
#
# range_counter += 1
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# # Pentagon
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / range_counter)
#
# range_counter += 1
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# # Hexagon
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / range_counter)
#
# range_counter += 1
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# # Heptagon
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / range_counter)
#
# range_counter += 1
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# # Octagon
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / range_counter)
#
# range_counter += 1
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# # Nonagon
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / range_counter)
#
# range_counter += 1
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# # Decagon
# for _ in range(range_counter):
#     tim.forward(100)
#     tim.right(360 / range_counter)
#
# range_counter += 1
# tim.setheading(0)
# tim.right(360 / range_counter)
# tim.color(get_random_color())
# counter += 1
#
# screen = Screen()
# screen.exitonclick()
