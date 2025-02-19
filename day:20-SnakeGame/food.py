from turtle import  Turtle, Screen
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

POSITIONS = [-300, 300]

class Food:
    def __init__(self):
        self.create_food()

    def create_food(self):
        dot = Turtle("square")
        dot.position(random.choice(POSITIONS), random.choice(POSITIONS))
        dot.color("white")