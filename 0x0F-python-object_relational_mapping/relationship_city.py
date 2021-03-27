#!/usr/bin/python3
"""
This module contains the class definition
of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """ City Class/Model inherit from Base"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
