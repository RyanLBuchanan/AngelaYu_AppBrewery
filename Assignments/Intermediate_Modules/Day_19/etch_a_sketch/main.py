import turtle
import random
from turtle import Turtle, Screen

# Set up the race
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Define the colors, user bet, and starting y positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()
y_positions = [-100, -50, 0, 50, 100, 150]

# Create the turtle instances
turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

# Check if the user has placed a bet
if user_bet:
    is_race_on = True

# Run the race
while is_race_on:
    for turtle in turtles:
        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!\n")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!\n")

        # Move each turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Function for exiting the program with the space bar
def exit_program():
    turtle.bye()

# Bind the exit program function to the space bar
screen.onkeypress(exit_program, "space")

# Generate random speeds for the turtles
random_speeds = []
for _ in range(6):
    random_move_param = random.randint(10, 50)
    random_speeds.append(random_move_param)

# Function to generate random color values
def get_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# Movement functions for the turtles
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
        turtle.right(random_move_param)

def clear():
    for turtle in turtles:
        turtle.clear()
        turtle.penup()
        turtle.home()

# Listen for key events
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
