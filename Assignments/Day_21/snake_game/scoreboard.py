from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 470)
        self.font = ("Press Start 2P", 16, "normal")
        self.write_score()

    def write_score(self):
        """
        Write the current score on the screen using the custom font.
        """
        self.clear()  # Clear any previously written score
        self.write(f"Score: {self.score}", align="center", font=self.font)

    def increase_score(self):
        """
        Increase the score by 1 and update the displayed score.
        """
        self.score += 1
        self.write_score()
