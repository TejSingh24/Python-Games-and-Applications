from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,360)
        self.write(arg='Score: {}, High Score: {}'.format(self.score, self.high_score),align=ALIGNMENT, font=FONT, move=False)

    def increase(self):
        self.clear()
        self.score += 1
        self.write(arg='Score: {}, High Score: {}'.format(self.score, self.high_score), move=False, align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.increase()


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg='GAME OVER', move=False, align=ALIGNMENT, font=FONT)