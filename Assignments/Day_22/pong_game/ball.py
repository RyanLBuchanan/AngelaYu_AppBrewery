from turtle import Turtle
import random

# Setup constants
MOVING_UP = 20


class Ball(Turtle):

    def __init__(self):
        """
        Initialize the Food class, which represents the food for the snake.

        The food is created as a blue circle shape with a smaller size than the default turtle size.
        It is positioned at a random location within the game screen.
        """
        super().__init__()  # Initialize the Turtle superclass
        self.shape("circle")  # Set the shape of the food to a circle
        self.color("yellow")  # Set the color of the food to blue
        self.penup()  # Lift the pen to prevent drawing lines
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()