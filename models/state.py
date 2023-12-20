#!/usr/bin/python3
"""This module contains one class State"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import shlex
from models.city import City


class State(BaseModel, Base):
    """the class for State
    Attributes:
    name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade='all, delete, delete-orphan',
            backref="state")
    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
