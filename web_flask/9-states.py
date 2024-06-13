#!/usr/bin/python3
"""
Starts a Flask web application:
- Listening on 0.0.0.0, port 5000
- Routes:
  /states: display a HTML page with a list of all State objects present in DBStorage sorted by name (A->Z)
  /states/<id>: display a HTML page with the State object present in DBStorage with the id linked to it, and its City objects sorted by name (A->Z)
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Displays a HTML page with a list of all State objects or specific State object by id present in DBStorage sorted by name (A->Z)"""
    states = storage.all(State)
    if id:
        state = states.get(f"State.{id}")
        return render_template('9-states.html', state=state)
    else:
        sorted_states = sorted(states.values(), key=lambda state: state.name)
        return render_template('9-states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
