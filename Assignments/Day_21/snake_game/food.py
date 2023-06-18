from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """
        Initialize the Food class, which represents the food for the snake.

        The food is created as a blue circle shape with a smaller size than the default turtle size.
        It is positioned at a random location within the game screen.
        """
        super().__init__()  # Initialize the Turtle superclass
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to prevent drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Scale the size of the food shape
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the animation speed of the food to the fastest
        self.refresh()  # Move the food to the random location

    def refresh(self):
        random_x = random.randint(-280, 280) # Generate x-coordinate within the game screen
        random_y = random.randint(-280, 280)  # Generate y-coordinate within the game screen
        self.goto(random_x, random_y)  # Move the food to the random location