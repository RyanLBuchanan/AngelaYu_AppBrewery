from turtle import Turtle
# import tkinter.font as tkFont
#
# font_path = "C:\Users\vreed\Desktop\Ryan\Fonts\press_start_2p"
# press_start_font = tkFont.Font(family="Press Start 2P", file=font_path)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("red")
        self.speed("fastest")
        self.goto(0, 470)
        self.score = 0
        self.font = ("Press Start 2P", 16, "normal")
        self.write_score()

    def write_score(self):
        """
        Write the current score on the screen using the custom font.
        """
        self.clear()  # Clear any previously written score
        self.write(f"Score: {self.score}", align="center", font=self.font)
