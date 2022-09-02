from turtle import Turtle, Screen, color, colormode
import random
import time


# lengt = input()
# leng = int(input("Length of dashed line: "))
# total_length = int(input("Total length of line: "))

# timmy = Turtle()
# timmy.shape("turtle")
my_screen = Screen()
print(my_screen.canvheight)
# timmy.color("blue")

#TODO: Draw a dashed line with the help of turtle


# def dashed_line(leng, total):
#     if total >= 2*leng:
#         timmy.forward(leng)
#         timmy.penup()
#         timmy.forward(leng)
#         timmy.pendown()
#         dashed_line(leng, total-2*leng)


# dashed_line(leng, total_length)
# dashed_line(leng, total_length+200)


#TODO: Draw multiple polygons with random color pens, for this upto decagon from triangle.


# color_list = ["CornflowerBlue", "DarkOrchid", 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']

# def n_gon_shape(n):
#     for i in range(n):
#         timmy.forward(100)
#         timmy.right(360/n)


# for i in range(3,11):
#     timmy.color(random.choice(color_list), "green")
#     n_gon_shape(i)


#TODO: Random Walk


# color_list = ["CornflowerBlue", "DarkOrchid", 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen', 'moccasin', 'magenta', 'green yellow']
# directions = [0, 90, 180, 270]
# distances = [10, 20, 15, 30, 40, 50, 25, 15, 35, 45]

# timmy.pensize(15)
# timmy.speed('fastest')
# colormode(255)

# def random_walk(n):
#     # timmy.color(random.choice(color_list))
#     timmy.pencolor((random.randint(1,255), random.randint(1,255), random.randint(1,255)))
#     timmy.setheading(random.choice(directions))
#     timmy.forward(random.randint(5,50))
#     random_walk(n-1)


# random_walk(6)


#TODO: Spirograph


# timmy.speed('fastest')
# colormode(255)

# def circle():
#     timmy.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#     timmy.circle(100, 150)
#     timmy.setheading(timmy.heading() + 90)

# for i in range(50):
#     circle()

#TODO: Event listner, key walk


# def pen_up():
#     if timmy.isdown() == True:
#         timmy.penup()
#     else:
#         timmy.pendown()


# def move_forward():
#     timmy.forward(10)


# def move_backward():
#     timmy.backward(10)


# def turn_right():
#     timmy.right(10)


# def turn_left():
#     timmy.left(10)


# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.penup()



# my_screen.listen()
# my_screen.onkey(key='space', fun=pen_up)
# my_screen.onkeypress(key='Up', fun=move_forward)
# my_screen.onkeypress(key='Down', fun=move_backward)
# my_screen.onkeypress(key='Right', fun=turn_right)
# my_screen.onkeypress(key='Left', fun=turn_left)

#TODO: Turtle Race Game


# my_screen.setup(height=800, width=800)

# color_list = ["violet", "indigo", 'blue', 'green', 'yellow', 'orange']
# initial_position = [-90, -60, -30, 30, 60, 90]

# def turtle_race_game():
#     racing_turtles = []
#     is_race_on = False
#     winner = ''
#     try_again = ''

#     user_bet = my_screen.textinput(title='Turtle Race Game', prompt='Choose your turtle color, Hope he wins')
#     if user_bet:
#         is_race_on = True

#     for turtle_number in range(0,6):
#         tim = Turtle(shape='turtle')
#         tim.color(color_list[turtle_number])
#         tim.penup()
#         tim.goto(x=-390, y=initial_position[turtle_number])
#         racing_turtles.append(tim)

#     while is_race_on:
#         for turtle in racing_turtles:
#             turtle.forward(random.randint(0,10))
#             if turtle.xcor() > 390:
#                 winner = turtle.pencolor()
#                 is_race_on = False
#                 break
        
#     if winner == user_bet:
#         try_again = my_screen.textinput(title='Turtle Race Ended', prompt="You've won!, {} colored turtle is the winner! \n Wanna try your luck again: ".format(winner))
#     elif winner != user_bet:
#         try_again = my_screen.textinput(title='Turtle Race Ended', prompt="You've lost!, {} colored turtle is the winner! \n Wanna try your luck again: ".format(winner))
        
#     if try_again.lower() == 'yes' or try_again.lower() == 'true':
#         my_screen.clearscreen()
#         turtle_race_game()
#     else:
#         my_screen.clearscreen()


# turtle_race_game()

timmy = Turtle()
print(timmy.heading())



my_screen.exitonclick()

