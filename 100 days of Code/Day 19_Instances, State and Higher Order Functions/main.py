from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500,500)

colors = ["red","black","orange","green","blue","purple"]
y_pos = [-70,-40,-10,20,50,80]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
while(user_bet not in colors):
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")



all_turtle = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230,y_pos[turtle_index])
    all_turtle.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've loss! The {win_color} turtle is the winner!")
        else:
            turtle.penup()
            turtle.forward(randint(0, 15))
        

screen.exitonclick()
