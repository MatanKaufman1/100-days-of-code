from turtle import Turtle

STARTING_POSITION = (0, 0)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=1)



