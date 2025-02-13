import turtle as turtle_module
import random

turtle_module.colormode(255)
screen = turtle_module.Screen()
screen.setup(width=600, height=800)

arrow = turtle_module.Turtle()
colors_list = [(134, 87, 113), (117, 151, 202), (83, 99, 138), (231, 138, 87), (189, 130, 162), (170, 101, 128), (99, 117, 177), (204, 94, 77), (167, 77, 62), (249, 210, 79), (186, 209, 238), (232, 163, 185), (251, 211, 164), (111, 37, 63), (172, 183, 225), (243, 165, 151), (235, 193, 211), (70, 26, 51), (230, 155, 15), (57, 55, 95), (31, 43, 70), (137, 32, 25), (245, 214, 3), (18, 82, 101), (80, 42, 39), (151, 204, 227), (81, 97, 95), (74, 141, 176), (31, 54, 51), (218, 239, 237), (171, 189, 188), (44, 76, 71), (169, 208, 205)]
arrow.speed("fastest")
arrow.hideturtle()
arrow.penup()
screen.screensize(20, 40)
arrow.setheading(225)
arrow.forward(350)
arrow.setheading(0)
number_of_dots = 400

for dot_count in range(1, number_of_dots +1):
    arrow.dot(20, random.choice(colors_list))
    arrow.forward(25)
    if dot_count % 20 == 0:
        arrow.setheading(90)
        arrow.forward(30)
        arrow.setheading(180)
        arrow.forward(500)
        arrow.setheading(0)


screen.exitonclick()