import turtle
import random

COLOR_LIST = [(232, 251, 242), (198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62)]

DOT_SIZE = 20
DISTANCE = 50
HEIGHT = 10
WIDTH = 10
SPEED = 0

direction_variable = 1

screen = turtle.Screen()
hirst = turtle.Turtle()

turtle.colormode(255)


def turn_left():
    hirst.setheading(180)


def turn_right():
    hirst.setheading(0)




def random_color():
    random_position = random.randint(0, len(COLOR_LIST)-1)
    return COLOR_LIST[random_position]


def change_row(direction):
    hirst.dot(DOT_SIZE, random_color())
    direction *= -1
    hirst.setheading(90)
    hirst.forward(DISTANCE)

    if direction == 1:
        turn_right()
    else:
        turn_left()

    return direction


def move_to_start_position():
    hirst.setheading(225)
    hirst.penup()
    hirst.forward(320)
    hirst.setheading(0)


move_to_start_position()
for _ in range(HEIGHT):
    for _ in range(WIDTH):
        hirst.dot(DOT_SIZE, random_color())
        hirst.forward(DISTANCE)
    direction_variable = change_row(direction_variable)
hirst.hideturtle()

screen.exitonclick()
