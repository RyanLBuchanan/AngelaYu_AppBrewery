import turtle
import random
from turtle import Turtle, Screen

from zmq import green


# Function to generate random color values
def get_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

turtles = []


for turtle_index in range(0, 5):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[turtle_index])
    turtles.append(turtle)
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")


# Function for exiting turtle with space bar
def exit_program():
    turtle.bye()


# Bind the exit program to the space bar
screen.onkeypress(exit_program, "space")

random_speeds = []
for _ in range(6):
    random_move_param = random.randint(10, 50)
    random_speeds.append(random_move_param)


def move_forwards():
    for turtle in turtles:
        turtle.forward(random_move_param)


def move_backwards():
    for turtle in turtles:
        turtle.backward(random_move_param)


def turn_left():
    for turtle in turtles:
        turtle.left(random_move_param)


def turn_right():
    for turtle in turtles:
        turn_right(random_move_param)


def clear():
    for _ in turtles:
        _.clear()
        _.penup()
        _.home()


screen.listen()


#Function as input
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()