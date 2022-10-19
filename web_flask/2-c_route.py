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

    app.run('0.0.0.0')
