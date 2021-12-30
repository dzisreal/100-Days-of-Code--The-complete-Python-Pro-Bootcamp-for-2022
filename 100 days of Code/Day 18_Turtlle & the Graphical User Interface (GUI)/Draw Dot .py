import turtle as t
from random import choice

tim = t.Turtle()
screen = t.Screen()

color_list = [(202, 164, 110), (149, 75, 50),
              (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]


def more_dots(x, y):
    """Draws a row of 10 dots."""
    for i in range(10):
        tim.goto(x, y)
        tim.dot(20, choice(color_list))
        x += 50


def main():
    """Main program function"""
    tim.hideturtle()
    tim.penup()
    tim.speed("fastest")
    x_pos = -225
    y_pos = -225
    screen.colormode(255)
    for i in range(10):
        more_dots(x_pos, y_pos)
        y_pos += 50

    screen.exitonclick()


main()