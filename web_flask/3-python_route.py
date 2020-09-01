#!/usr/bin/python3
""" Script to begin a flask application """
from flask import Flask
from string import Template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ view resp to display hello whn the strtd app is curled """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ view resp to display hbnb whn routed to /hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ view resp display value of text whn routed to /c/.. """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ view resp display phrase whn routed to python """
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
