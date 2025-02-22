from turtle import Turtle

STARTING_POSITION = (0, 0)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

   # def move_up(self):
   #     new_y = self.setposition.ycor() + 20
   #     self.goto(self.xcor(), new_y)

    #def move_down(self):
    #    new_y = self.setposition.ycor() - 20
    #    self.goto(self.xcor(), new_y)

    def go_up(self):
        new_y =  self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)