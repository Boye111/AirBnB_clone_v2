#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask

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

    app.run('0.0.0.0')
