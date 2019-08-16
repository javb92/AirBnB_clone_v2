#!/usr/bin/python3
""" NEW ENGINE FOR DATABASE SAVE
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """class DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """constructor method
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """all method
        """
        key_d = "_sa_instance_state"
        tmp_dict2 = {}
        if cls is not None:
            states = self.__session.query(cls).all()
            for item in states:
                key = str(cls.__name__) + "." + str(item2.id)
                if key_d in item.keys():
                    del item[key_d]
                tmp_dict2.update({key:item})
        else:
            clases = [State, City, User, Place, Review, Amenity]
            for item in clases:
                states = self.__session.query(item).all()
                for item2 in states:
                    key = str(item.__name__) + "." + str(item2.id)
                    tmp_dict2.update({key:item2})
        return tmp_dict2

    def new(self, obj):
        """add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current database session"""
        if obj:
            dele = session.query(type(obj)).filter(type(obj.id).like(obj.id))
            session.delete(dele)
            self.save()


    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))()
