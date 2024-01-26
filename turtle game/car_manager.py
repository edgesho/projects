from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.Cars=[]
        self.STARTING_MOVE_DISTANCE = 5

    def new_cars(self):
        ch=random.randint(1,6)
        if ch==2:
            new=Turtle()
            new.shape("square")
            new.color(random.choice(COLORS))
            new.shapesize(stretch_wid=1,stretch_len=2)
            new.penup()
            new.goto(300,random.randint(-260,260))
            self.Cars.append(new)

    def move_cars(self):
        for i in self.Cars:
            i.backward(self.STARTING_MOVE_DISTANCE)

    def next_level(self):

        self.STARTING_MOVE_DISTANCE+=MOVE_INCREMENT



