#!/usr/bin/python3
""" Script to begin a flask application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False, methods=["GET", "POST"])
def state_list():
    """ route to display a HTML page """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def tear_session(self):
    """ method to remove sqlalchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
