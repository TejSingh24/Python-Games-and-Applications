from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()


    def update(self):
        self.clear()
        self.goto(-100,260)
        self.write(arg=self.l_score,align=ALIGNMENT, font=FONT, move=False)
        self.goto(100,260)
        self.write(arg=self.r_score,align=ALIGNMENT, font=FONT, move=False)


    def l_point(self):
        self.l_score += 1
        self.update()


    def r_point(self):
        self.r_score += 1
        self.update()


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg='GAME OVER', move=False, align=ALIGNMENT, font=FONT)