from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Press Start 2P", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("orange")
        self.penup()

    def exit_program(self):
        """
        Exit the program with the space bar
        """
        self.head.screen.bye()