from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def clockwise():
    tim.right(10)


def c_clockwise():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=c_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
