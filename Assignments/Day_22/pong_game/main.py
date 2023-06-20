# Pong Game
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

PERIMETER_X = 1800
PERIMETER_Y = 900
PADDLE_X_MARGIN = PERIMETER_X/2 - 50
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

# Instantiate the scoreboard
scoreboard = Scoreboard()


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
    time.sleep(ball.move_speed)

    ball.move()

    # Exit on space bar for development
    screen.onkeypress(exit_program, "space")

    # Detect collisions with the walls
    if ball.ycor() > (PERIMETER_Y/2 - 20) or ball.ycor() < -(PERIMETER_Y/2 - 20):
        ball.bounce_y()

    # Detect r_paddle collisions and change ball direction
    if ball.distance(r_paddle) < 50 and ball.xcor() > 840 or ball.distance(l_paddle) < 50 and ball.xcor() < -840:
        ball.bounce_x()

    # Detect r_paddle misses
    if ball.xcor() > PERIMETER_X/2:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l_paddle misses
    if ball.xcor() < -(PERIMETER_X/2):
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()