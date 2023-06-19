from turtle import Turtle

# Create constants
MOVE_DISTANCE = 20
PADDLE_WIDTH = 5  # As a scalar of original turtle size, 20 x 20
PADDLE_LENGTH = 1  # As a scalar of original turtle size, 20 x 20

# Create Paddle class
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
