#!/usr/bin/python3
"""This module contains one class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel):
    """child class of the class BaseModel"""
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
