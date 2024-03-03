from turtle import Turtle, Screen

sketcher = Turtle()
window = Screen()


def move_forwards():
    sketcher.forward(10)


def move_backwards():
    sketcher.backward(10)


def tilt_left():
    heading = sketcher.heading() + 10
    sketcher.setheading(heading)


def tilt_right():
    heading = sketcher.heading() - 10
    sketcher.setheading(heading)


def reset():
    sketcher.clear()
    sketcher.penup()
    sketcher.home()
    sketcher.pendown()


window.listen()

window.onkeypress(move_forwards, "w")
window.onkeypress(move_backwards, "s")
window.onkeypress(tilt_left, "a")
window.onkeypress(tilt_right, "d")
window.onkeypress(reset, "c")

window.exitonclick()
