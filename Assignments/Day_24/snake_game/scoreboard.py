from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Press Start 2P", 16, "normal")
SCOREBOARD_COORDINATES = 0, 475


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(SCOREBOARD_COORDINATES)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Write the current score on the screen using the custom font.
        """
        self.clear()  # Clear any previously written score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score by 1 and update the displayed score.
        """
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def get_high_score(self):
    #     with open("data.txt", mode="r") as file:
    #         self.high_score = int(file.read())
    #     return self.high_score
    #
    # def set_high_score(self):
    #     with open("data.txt", mode="w") as file:
    #         file.write(str(self.high_score))
