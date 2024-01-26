from turtle import Turtle,Screen
from paddles import paddle
from ball import Ball
import time
from scoreboard import Scoreboard
score=Scoreboard()
right_paddle=paddle()
right_paddle.paddle_loc(370)
left_paddle=paddle()
left_paddle.paddle_loc(-370)
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Ping Pong")
screen.tracer(0)
ball=Ball()
screen.listen()
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")
screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"s")
on=True
speed=0.1
while on:
    time.sleep(speed)
    screen.update()

    ball.move()

    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()
    if ball.distance(right_paddle)<60 and ball.xcor()>335 or ball.distance(left_paddle)<60 and ball.xcor()<-335:
        ball.bounce_x()
        speed*=0.9
    if ball.xcor() > 400 :
       speed=0.1
       ball.reset_pos()
       score.update_left()
    if ball.xcor()<-400:
        ball.reset_pos()
        score.update_right()


screen.exitonclick()
