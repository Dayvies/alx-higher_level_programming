#!/usr/bin/python3
"""city model module"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City (Base):
    """city definition"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(
        'states.id', ondelete="CASCADE"), nullable=False)
    state = relationship("State", back_populates="cities")
