# Pong Game
from turtle import Screen

from Day_22.pong_game.ball import Ball
# TODO 1: Create the game window (screen) and set up the display

# from scoreboard.py import Scoreboard
from paddle import Paddle
from ball import Ball
import time

PERIMETER_X = 1800
PERIMETER_Y = 900
OUT_OF_BOUNDS = 788
GAME_BOARD_COLOR = "black"
PADDLE_X_POS, PADDLE_Y_POS = 800, 0

# Create game board (screen)
screen = Screen()
screen.setup(width=PERIMETER_X, height=PERIMETER_Y)
screen.bgcolor(GAME_BOARD_COLOR)
screen.title("My Pong")
screen.tracer(0)


# Create paddles
r_paddle = Paddle(PADDLE_X_POS, PADDLE_Y_POS)
l_paddle = Paddle(-PADDLE_X_POS, PADDLE_Y_POS)
# ball = Ball()


# Event listeners
screen.listen()
screen.onkey(r_paddle.r_go_up, "Up")
screen.onkey(r_paddle.r_go_down, "Down")
screen.onkey(l_paddle.l_go_up, "w")
screen.onkey(l_paddle.l_go_down, "s")


# Exit on space bar for development
def exit_program():
    """
    Exit the program with the space bar
    """
    screen.bye()


# Turn game board on by refreshing the screen
game_is_on = True
while game_is_on:
    # Update game board
    screen.update()

    # Delay ball movement for development
    time.sleep(0.1)


    screen.onkeypress(exit_program, "space")

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




screen.exitonclick()