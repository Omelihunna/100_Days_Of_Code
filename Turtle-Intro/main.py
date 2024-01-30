from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Cadetblue")


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    random_color = (R, G, B)
    tim.color(random_color)

def draw():
    global sides
    sides = 4
    while sides < 10:
        angle = 360 / sides
        for i in range(sides):
            tim.fd(100)
            tim.right(angle)
        change_color()
        sides += 1


draw()



# import heroes
# print(heroes.gen())





















screen = Screen()
screen.exitonclick()