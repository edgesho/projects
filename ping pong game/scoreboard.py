from turtle import Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-100, 250)
        self.write(self.left_score, align="center", font=("Algerian", 24, "normal"))
        self.goto(100, 250)
        self.write(self.right_score, align="center", font=("Algerian", 24, "normal"))

    def update_left(self):
        self.left_score+=1
        self.clear()
        self.update_scoreboard()
    def update_right(self):
        self.right_score+=1
        self.clear()
        self.update_scoreboard()

