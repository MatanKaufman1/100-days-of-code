import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard

# keyboard move:
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.cars_move()


    #Detect collision with car:
    for car in cars.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            score.game_over()

    # Detect player at the finish-line:
    if player.ycor() > 280:
        game_is_on = False
        score.winner()

screen.exitonclick()