from turtle import Turtle
import random

HEADING = [0, 180]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def reset_position_left(self):
        self.goto(0, 0)
        self.paddle_bounce()

    def reset_position_right(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.1
