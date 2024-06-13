#!/usr/bin/python3
"""
Starts a Flask web application:
- Listening on 0.0.0.0, port 5000
- Routes:
  /hbnb_filters: display a HTML page like 6-index.html, which was done during
  the project 0x01. AirBnB clone - Web static
    - Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css
    from web_static/styles/
    - Copy files icon.png and logo.png from web_static/images/
    - Update .popover div so it contains:
        - UL tag with the list of all State objects present in DBStorage
        sorted by name (A->Z)
        - LI tag: description of one State: <state.id>: <B><state.name></B> +
        UL tag: with the list of City objects linked to the State sorted by
        name (A->Z)
            - LI tag: description of one City: <city.id>: <B><city.name></B>
        - UL tag with the list of all Amenity objects present in DBStorage
        sorted by name (A->Z)
            - LI tag: description of one Amenity: <amenity.id>:
            <B><amenity.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page with filters for States and Amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template(
            '10-hbnb_filters.html',
            states=sorted_states,
            amenities=sorted_amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
