from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from Scoreboard import Scoreboard

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title(titlestring='Ping Pong Game')

screen.tracer(0)
score = Scoreboard()

def ping_pong_game():
    paddle1 = Paddle(380,0)
    paddle2 = Paddle(-390,0)
    screen.update()

    ball = Ball()

    screen.listen()
    game_is_on = True
    while game_is_on:
        screen.onkeypress(key='Up', fun=paddle1.move_up)
        screen.onkeypress(key='Down', fun=paddle1.move_down)
        screen.onkeypress(key='w', fun=paddle2.move_up)
        screen.onkeypress(key='s', fun=paddle2.move_down)

        ball.move()
        time.sleep(ball.move_speed)

        if ball.ycor() > 280 or ball.ycor() < -275:
            ball.y_bounce()

        if ball.xcor() > 365:
            if ball.distance(paddle1) < 55:
                ball.x_bounce()
            else:
                ball.move()
                screen.update()
                time.sleep(ball.move_speed)
                ball.move()
                screen.update()
                time.sleep(ball.move_speed)
                ball.reset()
                score.l_point()
        elif ball.xcor() < -375:
            if ball.distance(paddle2) < 55:
                ball.x_bounce()
            else:
                ball.move()
                screen.update()
                time.sleep(ball.move_speed)
                ball.move()
                screen.update()
                time.sleep(ball.move_speed)
                ball.reset()
                score.r_point()
        
        screen.update()
        
    # user_input = screen.textinput(title='Player {} won!'.format(winner), prompt='Do you want to try again? Yes/No')
    # if user_input.lower() == 'yes' or user_input.lower() == 'true':
    #     ball.reset()
    #     # screen.bgcolor('black')
    #     # ping_pong_game()
    # else:
    #     screen.bye()


ping_pong_game()



screen.exitonclick()