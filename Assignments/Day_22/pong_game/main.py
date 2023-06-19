# Pong Game
from turtle import Screen
# from scoreboard.py import Scoreboard
from paddle import Paddle
from ball import Ball
import time

from Day_22.pong_game.ball import Ball
# TODO 1: Create the game window (screen) and set up the display


PERIMETER_X = 1800
PERIMETER_Y = 900
PADDLE_X_MARGIN = PERIMETER_X/2 - 50
# OUT_OF_BOUNDS = 788
GAME_BOARD_COLOR = "black"
PADDLE_X_POS, PADDLE_Y_POS = 850, 0
UP, DOWN = 90, 270

# Create game board (screen)
screen = Screen()
screen.setup(width=PERIMETER_X, height=PERIMETER_Y)
screen.bgcolor(GAME_BOARD_COLOR)
screen.title("My Pong")
screen.tracer(0)


# Create paddles
r_paddle = Paddle((PADDLE_X_MARGIN, PADDLE_Y_POS))
l_paddle = Paddle((-PADDLE_X_MARGIN, PADDLE_Y_POS))
# Instantiate the ball
ball = Ball()


# Event listeners
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


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
    time.sleep(0.025)

    ball.move()

    # Exit on space bar for development
    screen.onkeypress(exit_program, "space")

    # Detect collisions with the walls
    if ball.ycor() > (PERIMETER_Y/2 - 20) or ball.ycor() < -(PERIMETER_Y/2 - 20):
        ball.bounce_y()

    # Detect r_paddle collisions and change ball direction
    if ball.distance(r_paddle) < 50 and ball.xcor() > 840 or ball.distance(l_paddle) < 50 and ball.xcor() < -840:
        print("Made contact with paddle")
        ball.bounce_x()
    elif ball.xcor() > PERIMETER_X/2 or ball.xcor() < -(PERIMETER_X/2):
        print("GAME OVER!")
        game_is_on = False

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