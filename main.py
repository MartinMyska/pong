from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
scr_width = 800
scr_height = 600
screen.setup(scr_width, scr_height)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle()
left_paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()

right_paddle.init_position(scr_width / 2 - 30)
left_paddle.init_position(-(scr_width / 2 - 30))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball_speed = 0.002

while True:
    screen.update()
    ball.move()
    time.sleep(ball.speeding)

    # detect wall collision
    if abs(ball.ycor()) > scr_height / 2 - 10:
        ball.wall_bounce()

    # detect paddle bounce
    if ((ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50)
       and abs(ball.xcor()) > scr_width / 2 - 50):
        ball.paddle_bounce()

    # right misses
    if ball.xcor() > scr_width / 2:
        ball.reset_position()
        scoreboard.l_scores()

    # left misses
    if ball.xcor() < -(scr_width / 2):
        ball.reset_position()
        scoreboard.r_scores()

screen.exitonclick()
