from turtle import Screen
from scoreboard import Scoreboard
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

# Create the scoreboard
scoreboard = Scoreboard()

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

    # Delay the movement so that it is easier to track snake during development
    time.sleep(0.1)

    # Move the snake
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 20:
        # Test collision with food as print statement
        # print("Nom, nom, nom!")
        food.refresh()

# Close the screen on click
screen.exitonclick()
