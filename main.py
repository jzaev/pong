from turtle import Screen
from paddles import Paddle
from ball import Ball
from time import sleep


def up_r():
    paddle_right.move(True)


def up_l():
    paddle_left.move(True)


def down_r():
    paddle_right.move(False)


def down_l():
    paddle_left.move(False)


def game():
    game_is_on = True
    while game_is_on:
        ball.move()
        screen.update()
        sleep(0.1)

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.reverse_y()

        if ball.xcor() > 380 or ball.xcor() < -380:
            game_is_on = False

        if ball.distance(paddle_right) < 50 and ball.xcor() > 360 or ball.distance(
                paddle_left) < 50 and ball.xcor() < -360:
            ball.reverse_x()

    if ball.xcor() > 0:
        return "right"
    else:
        return "left"


WIDTH = 800
HEIGHT = 600
TIMEOUT = 0.3
BORDER = 20

paddle_right = Paddle(WIDTH / 2 - BORDER)
paddle_left = Paddle(-WIDTH / 2 + BORDER)

screen = Screen()
screen.bgcolor("black")
screen.title("P O N G")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

screen.update()
screen.listen()
screen.onkey(up_r, "Up")
screen.onkey(down_r, "Down")
screen.onkey(up_l, "a")
screen.onkey(down_l, "z")

direction_x = 10
direction_y = 10

while True:
    ball = Ball(direction_x, direction_y)
    if game() == "left":
        direction_x = -10
    else:
        direction_x = 10
    ball.color("grey")

screen.exitonclick()
