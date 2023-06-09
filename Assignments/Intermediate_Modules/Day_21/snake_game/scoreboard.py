from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Press Start 2P", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 0)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Write the current score on the screen using the custom font.
        """
        self.clear()  # Clear any previously written score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score by 1 and update the displayed score.
        """
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Tell the user the game is over
        """
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
