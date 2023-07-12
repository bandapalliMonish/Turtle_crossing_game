import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
cars = CarManager()
score = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect collision with wall
    if player.ycor() > 280:
        cars.update()
        player.update_position()
        score.increase_level()

    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()


