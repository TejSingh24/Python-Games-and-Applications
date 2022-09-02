from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
print(my_screen.canvheight)

my_screen.setup(width=800, height=800)
my_screen.bgcolor('black')
my_screen.title(titlestring='The Snake Game')
my_screen.tracer(0)

food = Food()
score = Scoreboard()
snake = Snake(3)

my_screen.update()
my_screen.listen()
my_screen.onkeypress(key='Up', fun=snake.move_up)
my_screen.onkeypress(key='Down', fun=snake.move_down)
my_screen.onkeypress(key='Right', fun=snake.move_right)
my_screen.onkeypress(key='Left', fun=snake.move_left)


def create_border():
    timmy = Turtle()
    timmy.color('white')
    timmy.shapesize(stretch_len=0.25, stretch_wid=0.25)
    timmy.hideturtle()
    timmy.penup()
    my_screen.update()
    timmy.goto(-360, -360)
    timmy.pendown()
    my_screen.update()
    timmy.goto(360, -360)
    timmy.goto(360, 360)
    timmy.goto(-360, 360)
    timmy.goto(-360, -360)
    my_screen.update()

create_border()

game_is_on = True

while game_is_on:
    snake.move_forward()
    my_screen.update()
    time.sleep(0.1)

    # Detect collison with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.increase_length()

    # Detect Collision with wall
    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        game_is_on = False
        score.game_over() 

    #Detect collision with tail
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()




my_screen.exitonclick()