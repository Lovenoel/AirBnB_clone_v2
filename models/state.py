#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import city
from os import getenv


class State(BaseModel):
    """ State class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter method for cities when storage type is not db"""
            from models import storage
            city_list = []
            for city in storage.all(city).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
