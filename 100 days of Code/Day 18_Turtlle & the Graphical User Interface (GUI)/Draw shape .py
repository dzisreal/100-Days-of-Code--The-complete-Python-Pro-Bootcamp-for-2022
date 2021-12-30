from turtle import Turtle, Screen
import random
rua = Turtle()
rua.shape("turtle")
colors = ["lime","medium blue","dodger blue","red","yellow","medium violet red","medium spring green","slate gray"]
num_sides = 5

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        rua.forward(100)
        rua.right(angle)

for shape_side in range(3,11):
    rua.color(random.choice(colors))
    draw_shape(shape_side)






screen = Screen()
screen.exitonclick()