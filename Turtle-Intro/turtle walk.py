import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("Cadetblue")
tim.speed(10)

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [90, 180, 270, 360]
def walk():
    for i in range(150):
        x = random.choice(angles)
        tim.pensize(5)
        tim.pencolor(random.choice(colours))
        tim.fd(20)
        tim.setheading(x)



walk()