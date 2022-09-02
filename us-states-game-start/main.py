from tarfile import PAX_NAME_FIELDS
import turtle
import pandas as pd

data = pd.read_csv("app_brewery-365 days code\\us-states-game-start\\50_states.csv")

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'app_brewery-365 days code\\us-states-game-start\\blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
all_states = data.state.to_list()


timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed('fastest')

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name that you can remember:").title()
    if answer_state in ['Exit', 'Quit', 'No']:
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('app_brewery-365 days code\\us-states-game-start\\states_to_learn.csv')
        break

    if answer_state in all_states:
        timmy.goto(x=int(data[data.state == answer_state].x), y=int(data[data.state == answer_state].y))
        timmy.write(arg=answer_state)
        guessed_states.append(answer_state)


