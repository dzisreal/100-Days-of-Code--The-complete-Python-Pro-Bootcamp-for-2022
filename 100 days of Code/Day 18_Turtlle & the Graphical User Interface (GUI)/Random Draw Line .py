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

# colors = ["lime","medium blue","dodger blue","red","yellow","medium violet red","medium spring green","slate gray"]

directions = [0,90,180,270]
rua.pensize(10)
rua.speed("fastest")

for _ in range(200):
    rua.forward(30)
    rua.setheading(random.choice(directions))
    rua.color(random_color())
screen = Screen()
screen.exitonclick()