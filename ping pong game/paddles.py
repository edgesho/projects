from turtle import Turtle


class paddle(Turtle):
    def __init__(self):
        super().__init__()



    def paddle_loc(self,x):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,0)

    def move_up(self):
        y=self.ycor()
        self.goto(self.xcor(),y+50)

    def move_down(self):
        y=self.ycor()
        self.goto(self.xcor(),y-50)