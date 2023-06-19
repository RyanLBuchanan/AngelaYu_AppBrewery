# Pong Game
from turtle import Screen
# TODO 1: Create the game window (screen) and set up the display

# from scoreboard.py import Scoreboard
# from paddle1.py import Paddle1
# from paddle2 import Paddle2
# from ball import Ball
import time

PERIMETER_X = 1920
PERIMETER_Y = 1080
OUT_OF_BOUNDS = 788
GAME_BOARD_COLOR = "black"

# Create game board (screen)
screen = Screen()
screen.setup(width=PERIMETER_X, height=PERIMETER_Y)
screen.bgcolor(GAME_BOARD_COLOR)
screen.title("My Pong", )
screen.tracer(0)

# Event listeners
screen.listen()

# Create


# TODO 2a and 2b: Create the paddle objects for both players

# TODO 3: Create the ball object and set its initial position and movement

# TODO 4: Detect collisions with walls and bounce

# TODO 5: Detect paddle collisions and change ball direction

# TODO 6: Detect when paddles misses ball

# TODO 7: Keep score

# TODO 8: Add game logic to control game flow, such as starting, pausing, and ending

    # TODO: Handle user input

    # TODO: Move the paddles

    # TODO: Move the ball

    # TODO: Check for collisions

    # TODO: Update the score

    # TODO: Check for game over condition


# Close screen with space bar
def exit_program():
    """
    Exit the program with the space bar
    """
    screen.bye()


screen.onkeypress(exit_program, "space")

screen.exitonclick()