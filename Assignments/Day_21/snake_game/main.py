from turtle import Screen
from snake import Snake
from food import Food
import time

# Create the screen
screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create the snake
snake = Snake()

# Create the food
food = Food()

# Events listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Bind the exit program function to the space bar
screen.onkeypress(snake.exit_program, "space")

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
