import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scores = Scoreboard()
game_is_on = True


screen.listen()
screen.onkey(player.up, "Up")
while game_is_on:
    cars.create()
    cars.move()
    time.sleep(0.1)
    screen.update()

    #Detect Collision with Car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scores.game_over()

        if player.is_at_finish_line():
            player.go_to_start()
            cars.level_up()
            scores.increase_level()


screen.exitonclick()
