from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

score = Scoreboard()
paddle = Paddle
screen = Screen()
ball = Ball()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0)


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
    time.sleep(ball.move_speed)
    score.update_scoreboard()
    ball.move()
    if score.l_score == 3 or score.r_score == 3:
        game_is_on = False
        score.game_over()

    #Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    #Detect if score:
    if ball.xcor() > 390:
        score.l_point()
        ball.reset_position_left()

    if ball.xcor() < -390:
        score.r_point()
        ball.reset_position_right()


screen.exitonclick()

