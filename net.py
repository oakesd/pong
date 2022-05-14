from turtle import Turtle

from settings import MIN_Y, MAX_Y, NET_LENGTH, NET_GAP, UP


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.goto(0, MIN_Y)
        self.setheading(UP)
        self.draw()
        self.hideturtle()

    def draw(self):
        while int(self.ycor()) < MAX_Y:
            self.pd()
            self.forward(NET_LENGTH)
            self.pu()
            self.forward(NET_GAP)
