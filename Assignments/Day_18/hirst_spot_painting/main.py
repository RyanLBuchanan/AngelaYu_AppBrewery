import turtle as t
import random
from colorgram_extraction import color_list

# print(len(color_list))
tim = t.Turtle()
# t.pensize(1)

t.colormode(255)
# Create turtle screen
screen = t.Screen()
# screen.setup(1000, 1000)


# Function for exiting turtle with space bar
def exit_program():
    t.bye()


# Bind the exit program to the space bar
screen.onkeypress(exit_program, "space")

# Enable listening for key events
screen.listen()

x_offset = 25
y_offset = 25

number_of_dots = 20

# Set turtles starting x coordinate
# Set the turtle's initial position to the top-left corner
def reset_location(x_offset, y_offset):
    tim.penup()
    tim.goto(-screen.window_width() / 2  + x_offset, screen.window_height() / 2 - y_offset)
    tim.pendown()


# TODO 1: Create 10 x 10 painting of dots
def draw_line_of_dots():
    for _ in range(number_of_dots):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()

for _ in range(number_of_dots):
    reset_location(x_offset, y_offset)
    draw_line_of_dots()
    # x_offset += 50
    y_offset += 50

screen.exitonclick()