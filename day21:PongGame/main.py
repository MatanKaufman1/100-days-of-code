from turtle import Turtle, Screen

paddle = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

# key_move:
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down,"Down")



# shape:
paddle.shape("square")
paddle.shapesize(stretch_wid=6, stretch_len=1)
paddle.setposition(x=350, y=0)
paddle.color("white")




screen.exitonclick()

