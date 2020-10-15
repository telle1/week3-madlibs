"""A madlib game that compliments its users."""

from random import choice, sample, randint

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template('start_here.html')


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, randint(1, 3))

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():

    play_game = request.args.get("play")

    if play_game == "yes":
        return render_template('game.html')
    else:
        return render_template('goodbye.html')

@app.route('/madlib')
def show_madlib():

    name = request.args.get('name')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')
    adj2 = request.args.getlist('adj2')
    madlib_choice = ['madlib.html', 'madlib2.html']

    return render_template(choice(madlib_choice), color = color,
    noun = noun, adjective = adjective, person = name,
    adjective2 = adj2)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0", port=5000)
