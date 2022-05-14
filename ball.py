from turtle import Turtle
import random

HEADING_MODIFIER = [-1, 1]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("lime")
        self.move_speed = 0.1
        self.move_x = 10
        self.move_y = 10
        self.random_heading()
        self.pu()

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_x *= -1
        self.increase_speed()

    def bounce_y(self):
        self.move_y *= -1

    def hide(self):
        self.hideturtle()

    def random_x(self):
        self.move_x *= random.choice(HEADING_MODIFIER)

    def random_y(self):
        self.move_y *= random.choice(HEADING_MODIFIER)

    def random_heading(self):
        self.random_x()
        self.random_y()

    def respawn(self):
        self.goto(0, 0)
        self.bounce_x()
        self.random_y()
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= .9

    def decrease_speed(self):
        self.move_speed *= 1.1
