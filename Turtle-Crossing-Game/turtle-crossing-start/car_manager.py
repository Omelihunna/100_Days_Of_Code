COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y_pos = random.randint(-240, 240)
            color_choice = random.choice(COLORS)
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(color_choice)
            new_car.penup()
            new_car.goto(350, y_pos)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    pass
