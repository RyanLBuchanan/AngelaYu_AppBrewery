from turtle import Screen, Turtle
from snake import Snake
import time

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create the snake
snake = Snake()

game_is_on = True
while game_is_on:
    # Update the screen
    screen.update()

    # Delay the movement
    time.sleep(0.1)

    # Move the snake
    snake.move()

# Close the screen on click
screen.exitonclick()