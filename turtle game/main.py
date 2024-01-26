import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
Score=Scoreboard()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")
cars = CarManager()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.new_cars()
    cars.move_cars()
    for i in cars.Cars:
        if player.distance(i) < 20:
            Score.game_over()
            game_is_on = False
    if player.ycor()>270:
        player.reset_pos()
        player.clear()
        cars.next_level()
        Score.level_up()
screen.exitonclick()