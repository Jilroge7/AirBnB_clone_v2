#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """ Get value for cities """
        cityList = []
        cityAll = models.storage.all(City)
        for city in cityAll.values():
            if city.state_id == self.id:
                cityList.append(city)
        return cityList
