from turtle import Turtle

LENGTH = 80
TURTLE_SIZE = 20


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x, 0)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move(self, move_up=True):
        direction = 1 if move_up else -1
        self.goto(self.xcor(), self.ycor() + direction * 20)
