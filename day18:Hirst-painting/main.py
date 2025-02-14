import turtle as turtle_module
import random
from colorsExtract import color_extract

turtle_module.colormode(255)
screen = turtle_module.Screen()
screen.setup(width=600, height=800)

arrow = turtle_module.Turtle()
colors_list = color_extract()

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