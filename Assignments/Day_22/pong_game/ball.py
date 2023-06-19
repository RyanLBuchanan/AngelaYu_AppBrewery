from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """
        Initialize the Food class, which represents the food for the snake.

        The food is created as a blue circle shape with a smaller size than the default turtle size.
        It is positioned at a random location within the game screen.
        """
        super().__init__()  # Initialize the Turtle superclass
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to prevent drawing lines
        self.shapesize(stretch_len=1, stretch_wid=1)  # Scale the size of the food shape
        self.color("yellow")  # Set the color of the food to blue
        self.speed("fastest")  # Set the animation speed of the food to the fastest