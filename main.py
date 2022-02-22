# Day 22 Project Pong Arcade game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with roof or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    # Right wall collision
    if ball.xcor() > 380:
        score.left_point()
        score.update_score()
        ball.reset_position()
        ball.move()

    # Left wall collision
    if ball.xcor() < -380:
        score.right_point()
        score.update_score()
        ball.reset_position()
        ball.move()

    if score.left_score == 3:
        game_on = False
        score.winner("LEFT PLAYER WINS!")
    elif score.right_score == 3:
        game_on = False
        score.winner("RIGHT PLAYER WINS!")

screen.exitonclick()
