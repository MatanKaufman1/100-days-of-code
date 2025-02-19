from turtle import Turtle, Screen
import random
import time

screen = Screen()
snake = Turtle("square")

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
snake_length = 3
segment_list = []

for position in starting_position:
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    segment_list .append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segment_list) -1, 0, -1):
        new_x = segment_list[seg_num -1].xcor()
        new_y = segment_list[seg_num].ycor()
        segment_list[seg_num].goto(new_x, new_y)
    segment_list[0].forward(20)



screen.exitonclick()