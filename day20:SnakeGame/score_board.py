from turtle import  Turtle

ALIGNMENT = "center"
FONT = 'Courier', 10, "normal"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0, 280)
        self.score = 0
        self.color("white")
        self.score_update()


    def score_update(self):
        self.write(f"SCORE = {self.score}", align=ALIGNMENT, font= FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.setposition(0,0)
        self.clear()
        self.write(f"GAME OVER\nSCORE: {self.score}", align= ALIGNMENT, font= FONT)






