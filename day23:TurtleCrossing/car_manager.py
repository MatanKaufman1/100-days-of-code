from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RESPOND_X = 320


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.initial_cars_position()


    def initial_cars_position(self):
        for _ in range (20):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            x = random.randint(-300, 300)
            y = random.randint(-250, 270)
            new_car.setposition(x, y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -290:
                new_y = random.randint(-260, 270)
                car.setposition(RESPOND_X, new_y)







