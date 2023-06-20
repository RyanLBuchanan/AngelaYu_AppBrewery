from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 1
CAR_LENGTH = 3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.speed("fastest")
        self.goto(300, random.randint(-240, 240))
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        """
        Move the car to the left.
        """
        self.forward(self.move_distance)
