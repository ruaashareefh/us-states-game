import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
text = turtle.Turtle()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
data = pandas.read_csv("50_states.csv")
state_names = data["state"].to_list()
x_cor_list = data["x"].to_list()
y_cor_list = data["y"].to_list()
correct_guesses = []

while game_is_on:
    if len(correct_guesses) < 1:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another states name?").title()
    else:
        answer_state = screen.textinput(title=f"{correct_count}/50 States Correct", prompt="What's another states name?").title()

    if answer_state == "Exit":
        break
    if answer_state in state_names and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        correct_count = len(correct_guesses)
        index = state_names.index(answer_state)
        x_cor = x_cor_list[index]
        y_cor = y_cor_list[index]
        text.hideturtle()
        text.penup()
        text.goto(x_cor, y_cor)
        text.write(answer_state)
    if len(correct_guesses) == 50:
        game_is_on = False


states_to_learn = [state for state in state_names if state not in correct_guesses]
data2 = pandas.DataFrame(states_to_learn)
data2.to_csv("states_to_learn.csv")



