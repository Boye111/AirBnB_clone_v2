#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """ returns Hello HBNB! """
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """ returns HBNB """
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c(text):
        """ displays c followed by some text """
        return 'C ' + text.replace('_', ' ')

    @app.route('/python/')
    @app.route('/python/<text>', strict_slashes=False)
    def python(text="is cool"):
        """ display “Python ”, followed by the value of the text """
        return 'Python ' + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        """ display “n is a number” only if n is an integer """
        return str(n) + ' is a number'

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """ display a HTML page only if n is an integer """
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        """ H1 tag: “Number: n is even|odd” inside the tag BODY """
        parity = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """ states_list: display a HTML page: (inside the tag BODY """
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)

    @app.teardown_appcontext
    def teardown_db(error):
        """ closes db at the end of a request """
        storage.close()

    app.run('0.0.0.0')
