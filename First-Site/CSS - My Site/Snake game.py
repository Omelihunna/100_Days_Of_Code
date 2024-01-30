from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0, 1)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()
# tom = Turtle(shape="square")
# tom.color("white")
# tom.shapesize(stretch_wid=1, stretch_len=3)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.penup()
        seg.forward(20)
        time.sleep(1)

# while game_is_on:
#     tom.penup()
#     tom.speed(1)
#     tom.forward(10)







screen.exitonclick()