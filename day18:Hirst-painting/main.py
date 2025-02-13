import turtle as turtle_module
import random

turtle_module.colormode(255)
screen = turtle_module.Screen()
screen.setup(width=600, height=800)

arrow = turtle_module.Turtle()
colors_list = [(152, 56, 129), (130, 84, 216), (121, 27, 85), (178, 86, 164), (72, 25, 148), (217, 119, 186), (251, 151, 197), (96, 8, 50), (101, 53, 184), (167, 116, 239), (249, 125, 98), (181, 54, 43), (219, 87, 70), (145, 26, 22), (254, 173, 226), (254, 148, 135), (86, 0, 0), (190, 133, 251)]

arrow.speed("fastest")
arrow.hideturtle()
arrow.penup()
screen.screensize(0, 0, '#FFFFE0')
arrow.setheading(225)
arrow.forward(350)
arrow.setheading(0)
number_of_dots = 400

for dot_count in range(1, number_of_dots +1):
    arrow.dot(19, random.choice(colors_list))
    arrow.forward(25)
    if dot_count % 20 == 0:
        arrow.setheading(90)
        arrow.forward(30)
        arrow.setheading(180)
        arrow.forward(500)
        arrow.setheading(0)


screen.exitonclick()