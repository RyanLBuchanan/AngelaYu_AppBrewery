import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Create the turtle or snake instances
snake_sections = []
x_positions = [n * -20 for n in range(3)]

for snake_index in range(0, 3):
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.color("white")
    new_snake.goto(x=x_positions[snake_index], y=0)
    snake_sections.append(new_snake)


# Function for exiting the program with the space bar
def exit_program():
    turtle.bye()


# Bind the exit program function to the space bar
screen.onkeypress(exit_program, "space")

screen.listen()

screen.exitonclick()
