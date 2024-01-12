from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media4.giphy.com/media/7PqDpUepjFkBXr3ZK9/giphy.gif" width="480" height="480">')


the_number = random.randint(0, 9)


# def random_decorator(function):
#     def wrapper():
#         check_number(random_number=the_number)
#     return wrapper


@app.route("/<number>")
# @random_decorator
def check_number(number):
    global the_number
    number = int(number)
    if number == the_number:
        the_number = random.randint(0, 9)
        return ("<h1>You guessed right! Congratulations!</h1>"
                "<h1>Feel free to try again :)</h1>"
                "<h3>Remember to enjoy the game</h3>"
                "<img src='https://media2.giphy.com/media/s7Yo6tZqZEGw2ciiXr/giphy.gif'>")
    if number > the_number:
        return ("<h1>You guessed too high</h1>"
                "<img src='https://media4.giphy.com/media/xThuWvs0UTYRNvalAQ/giphy.gif?cid=ecf05e47otv4uoiskupy0zqlmg1187jr81v0pezd411lzchv&ep=v1_gifs_related&rid=giphy.gif&ct=g'>")
    if number < the_number:
        return ("<h1>You guessed too low</h1>"
                "<img src='https://media1.giphy.com/media/evIQwMHLwfFAY/giphy.gif?cid=ecf05e47p9mv73qlle2n9clivm3vkfjympiy7z6fsz451dfv&ep=v1_gifs_related&rid=giphy.gif&ct=g'>")
    else:
        return "<h1>Error: Check your syntax</h1>"


app.run(debug=True)
