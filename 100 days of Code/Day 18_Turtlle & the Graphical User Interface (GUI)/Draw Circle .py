from turtle import Turtle, Screen
import random
import turtle
rua = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return  (r,g,b)

rua.shape("turtle")

rua.pensize(2)
rua.speed("fastest")

def draw_spirograph(size_of_graph):
    for _ in range(360//size_of_graph):
        rua.color(random_color())
        rua.circle(size_of_graph*20)
        rua.setheading(rua.heading()+size_of_graph)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()