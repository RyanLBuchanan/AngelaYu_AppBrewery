import random
import turtle
from turtle import Turtle, Screen

""" N-gons in range(3 - 10)"""
tim = Turtle()

# Function to generate random color values
def get_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# Increase the pensize by a factor of 10
tim.pensize(tim.pensize() * 10)


#Make turtle walk faster
tim.speed(10)

#Make turtle walk a short 90 degree segment and turn and walk and turn -> all random
def walk_and_turn():
    for _ in range(10):
        distance = 40
        angle = random.choice([90, -90])
        tim.color(get_random_color())
        tim.forward(distance)
        tim.right(angle)


while True:
    walk_and_turn()

screen = Screen()
screen.exitonclick()