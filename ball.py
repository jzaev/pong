from turtle import Turtle


class Ball(Turtle):

    def __init__(self,x ,y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.speed = 1
        self.direction_x = x
        self.direction_y = y

    def move(self):
        new_x = self.xcor() + self.direction_x * self.speed
        new_y = self.ycor() + self.direction_y * self.speed
        self.goto(new_x, new_y)

    def reverse_y(self):
        self.direction_y = - self.direction_y


    def reverse_x(self):
        self.direction_x = - self.direction_x
        self.speed += 0.2
