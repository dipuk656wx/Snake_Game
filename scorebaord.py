from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()


        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    def increase_s(self):
        self.score += 1
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
    def update_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


