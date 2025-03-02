from turtle import  Turtle


FONT = ("Courier", 20, "normal")
POSITION = (-200, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.setposition(POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level +=1
        self.update_score()

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f"Game-Over\nLevel:{self.level}", align="center", font=FONT)
        self.level = 0

