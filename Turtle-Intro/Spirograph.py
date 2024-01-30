import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("Cadetblue")
tim.speed("fastest")

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    random_color = (R, G, B)
    tim.color(random_color)

def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        change_color()

spirograph(5)

screen = t.Screen()
screen.exitonclick()
