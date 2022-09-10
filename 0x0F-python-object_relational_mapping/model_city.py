#!/usr/bin/python3
"""city model module"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City (Base):
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
