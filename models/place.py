#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy import Table
from sqlalchemy.orm import relationship
import models
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """getter
            """
            dict_tmp = models.storage.all(models.Review)
            list_tmp = []
            for key, value in dict_tmp:
                if value.place_id == self.id:
                    list_tmp.append(value)
            return list_tmp

    @property
    def amenities(self):
        """getter amentities
        """
        list_amenity = []
        dic_tmp = models.storage.all(models.Amenity)
        for key, value in dic_tmp.items():
            for amenity in self.amenity_ids:
                if value.id == amenity:
                    print("AGREGADO REGISTRO")
                    list_amenity.append(value)
        return list_amenity

    @amenities.setter
    def amenities(self, obj):
        """ setter amenities
        """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
