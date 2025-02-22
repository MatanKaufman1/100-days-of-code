from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


#paddle = Turtle()
paddle = Paddle
screen = Screen()
ball = Ball()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

# shape:
#paddle.shape("square")
#paddle.penup()
#paddle.color("white")
screen.tracer(0)
#paddle.shapesize(stretch_wid=6, stretch_len=1)
#paddle.setposition(x=350, y=0)

r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))

#key_move:



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down,"S")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()

