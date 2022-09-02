from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SHAPE = 'circle'

class Snake():
    def __init__(self, length) -> None:
        self.snake = []
        self.length = length
        self.create_snake()
        self.head = self.snake[0]

    
    def create_snake(self):
        for i in range(0, self.length):
            box = Turtle(shape=SHAPE)
            box.color('white')
            box.penup()
            box.goto(x=-i*20, y=0)
            self.snake.append(box)


    def add_snake(self):
        box = Turtle(shape=SHAPE)
        box.color('white')
        box.penup()

        if self.head.heading() == float(UP):
            box.goto(x=self.snake[self.length-1].xcor(), y=self.snake[self.length-1].ycor()-20)

        if self.head.heading() == float(DOWN):
            box.goto(x=self.snake[self.length-1].xcor(), y=self.snake[self.length-1].ycor()+20)

        if self.head.heading() == float(RIGHT):
            box.goto(x=self.snake[self.length-1].xcor()-20, y=self.snake[self.length-1].ycor())

        if self.head.heading() == float(LEFT):
            box.goto(x=self.snake[self.length-1].xcor()+20, y=self.snake[self.length-1].ycor())
        
        self.snake.append(box)


    def move_snake(self):
        for seg in range(self.length-1, 0, -1):
            self.snake[seg].goto(x=self.snake[seg-1].xcor(), y=self.snake[seg-1].ycor())
            # time.sleep(0.1)


    def move_forward(self):
        self.move_snake()
        self.head.forward(20)


    def move_right(self):
        if self.head.heading() != LEFT:
            self.move_snake()
            self.head.setheading(RIGHT)
            self.head.forward(20)
        # time.sleep(0.1)

    
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.move_snake()
            self.head.setheading(LEFT)
            self.head.forward(20)
        # time.sleep(0.1)


    def move_up(self):
        if self.head.heading() != DOWN:
            self.move_snake()
            self.head.setheading(UP)
            self.head.forward(20)
        # time.sleep(0.1)

        
    def move_down(self):
        if self.head.heading() != UP:
            self.move_snake()
            self.head.setheading(DOWN)
            self.head.forward(20)
        # time.sleep(0.1)


    def increase_length(self):
        self.add_snake()
        self.length += 1




