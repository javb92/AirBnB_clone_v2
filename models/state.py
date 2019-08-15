#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        dict_tmp = models.storage.all(models.City)
        list_tmp = []
        for key, value in dict_tmp.items():
            if value.state_id == self.id:
                list_tmp.append(value)
        return list_tmp
