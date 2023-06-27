from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Press Start 2P", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Write the current score on the screen using the custom font.
        """
        self.clear()  # Clear any previously written score
        self.goto(-100, 400)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 400)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()