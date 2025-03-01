from turtle import  Turtle


FONT = ("Courier", 24, "normal")
POSITION = (0, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.setposition(POSITION)
        self.write(self.winner(), align="center", font=FONT)


    def winner(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.clear()
        self.score = 0

