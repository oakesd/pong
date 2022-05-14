from turtle import Turtle

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_SIZE = 16
FONT_WEIGHT = "bold"
NORMAL = (FONT_NAME, FONT_SIZE, FONT_WEIGHT)
LARGE = (FONT_NAME, FONT_SIZE * 2, FONT_WEIGHT)


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.score = 0
        self.pu()
        self.goto(position[0], position[1])
        self.hideturtle()
        self.update()

    def update(self):
        self.write(arg=self.score, align=ALIGNMENT, font=NORMAL)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        text = "GAME OVER"
        self.write(arg=text, align=ALIGNMENT, font=LARGE)

