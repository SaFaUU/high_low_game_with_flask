from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)
print(random_number)


@app.route("/")
def hello_world():
    return '<h1 style="color:orange;">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guessed_number>")
def show_result(guessed_number):
    if guessed_number == random_number:
        return '<h1 style="color:blue;">You Guessed Correct</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

    elif guessed_number > random_number:
        return '<h1 style="color:purple;">Your Guess is Too High</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color:green;">Too Low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run()
