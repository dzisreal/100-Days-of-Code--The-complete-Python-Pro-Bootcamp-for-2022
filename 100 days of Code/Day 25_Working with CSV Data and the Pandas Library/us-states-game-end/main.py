import turtle
import pandas
import os

#Tro link ve folder nay thi moi dung link gon cua anh voi file csv duoc
os.chdir("C:/Users/Admin/Desktop/100 days of Code/Day 25_Working with CSV Data and the Pandas Library/us-states-game-end")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) #Dinh dang kich thuoc app bang kich thuoc anh
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
