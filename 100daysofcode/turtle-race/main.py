from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500,height=400)
user_guess = screen.textinput(title="Make your bet on turtle", prompt="Enter winner (color):")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
height = 125
for turtle_index in range(0, len(colors)):
    racer = Turtle("turtle")
    racer.color(colors[turtle_index])
    racer.penup()
    racer.goto(x=-220,y=height)
    height -= 50

screen.exitonclick()
# commit didn't work
