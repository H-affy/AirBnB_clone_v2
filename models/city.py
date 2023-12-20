#!/usr/bin/python3
"""This module contains one class City"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """the class for City
    Attributes:
    state_id: The state id
    name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    laces = relationship(
            "Place", cascade='all, delete, delete-orphan',
            backref="cities")
