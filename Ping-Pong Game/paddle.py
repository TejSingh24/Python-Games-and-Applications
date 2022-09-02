from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, distance_x, distance_y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.goto(x=distance_x, y=distance_y)



    def move_up(self):
        self.forward(20)


    def move_down(self):
        self.backward(20)


