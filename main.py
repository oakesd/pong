import time
from turtle import Screen

from ball import Ball
from net import Net
from paddle import Paddle
from score import Score
from settings import WIDTH, HEIGHT, P1_POSITION, P2_POSITION, S1_POSITION, S2_POSITION, \
    MIN_Y, MAX_Y

game_on = True


def pause():
    global game_on
    if game_on:
        game_on = False
        screen.exitonclick()
    else:
        game_on = True
        play()


net = Net()
p1 = Paddle(P1_POSITION)
p2 = Paddle(P2_POSITION)
s1 = Score(S1_POSITION)
s2 = Score(S2_POSITION)
ball = Ball()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("PONG")
screen.tracer(0)

screen.listen()
screen.onkeypress(p1.up, "w")
screen.onkeypress(p1.down, "s")
screen.onkeypress(p2.up, "Up")
screen.onkeypress(p2.down, "Down")
screen.onkey(pause, "Escape")
screen.onkey(pause, "space")


def play():
    while game_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # detect collision with paddle 1
        if ball.distance(p1) < 50 and ball.xcor() < p1.xcor() + 40:
            ball.bounce_x()

        # detect collision with paddle 2
        if ball.distance(p2) < 50 and ball.xcor() > p2.xcor() - 40:
            ball.bounce_x()

        # detect collision with top or bottom of screen
        if ball.ycor() > MAX_Y - 40 or ball.ycor() < MIN_Y + 40:
            ball.bounce_y()

        # detect p1 score
        if ball.xcor() > p2.xcor():
            s1.increase_score()
            ball.respawn()

        if ball.xcor() < p1.xcor():
            s2.increase_score()
            ball.respawn()


play()
