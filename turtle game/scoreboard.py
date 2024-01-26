from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.score()
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
    def score(self):
        self.penup()
        self.goto(-270,270)
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def level_up(self):
        self.level+=1
        self.clear()
        self.score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)