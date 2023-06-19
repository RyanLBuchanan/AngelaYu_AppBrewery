from turtle import Turtle

# Create constants
MOVE_DISTANCE = 20
PADDLE_WIDTH = 5 # As a scalar of original turtle size, 20 x 20
PADDLE_LENGTH = 1 # As a scalar of original turtle size, 20 x 20

# Create Paddle class
class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(x_pos, y_pos)
        self.shapesize(stretch_wid=PADDLE_WIDTH,
                       stretch_len=PADDLE_LENGTH)
        self.speed("fastest")

    def r_go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def r_go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def l_go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def l_go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # # Close screen with space bar
    # def exit_program(self):
    #     """
    #     Exit the program with the space bar
    #     """
    #     self.screen.bye()
