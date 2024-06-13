#!/usr/bin/python3
"""
Starts a Flask web application:
- Listening on 0.0.0.0, port 5000
- Routes:
  /states_list: display a HTML page: (inside the tag BODY)
    - H1 tag: “States”
    - UL tag: with the list of all State objects present in DBStorage sorted 
    by name (A->Z)
        - LI tag: description of one State: <state.id>: <B><state.name></B>
  /cities_by_states: display a HTML page: (inside the tag BODY)
    - H1 tag: “States”
    - UL tag: with the list of all State objects present in DBStorage sorted
    by name (A->Z)
        - LI tag: description of one State: <state.id>: <B><state.name></B> +
        UL tag: with the list of City objects linked to the State sorted by
        name (A->Z)
            - LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of all State objects present in
    DBStorage sorted by name (A->Z)"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a HTML page with a list of all State objects and their related
    City objects present in DBStorage sorted by name (A->Z)"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

