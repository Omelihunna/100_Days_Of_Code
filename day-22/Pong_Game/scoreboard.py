from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 48, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("black")
        self.penup()
        self.goto(0, 200)
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.l_score} : {self.r_score}", move=False, align=ALIGNMENT, font=FONT)

    def l_score_count(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_score_count(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)