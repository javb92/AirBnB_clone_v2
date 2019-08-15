#!/usr/bin/python3
""" NEW ENGINE FOR DATABASE SAVE
"""
from sqlalchemy import (create_engine)
import os

class DBStorage():
    """class DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """constructor method
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_DB')), pool_pre_ping=True)
        os.environ.get('HBNB_MYSQL_DB').create_all(engine)
        Session = sessionmaker(bind=engine)
        self.__session = Session()
        if os.environ.get('HBNB_ENV') == "test":
            os.environ.get('HBNB_MYSQL_DB').metadata.drop_all(bind=engine)

    def all(self, cls=None):
        tmp_dict2 = {}
        if cls is not None:
            states = session.query(cls).all()
            for item in states:
                print("//////ALL////")
                print(item)
                tmp_dict2.update({cls.__name__:states})
            print("//////FINISH ALL/////")
        else:
            states = session.query(User, State, City, Amenity, Place, Review).all()
        tmp_dict2.update({:})
        return

    def new(self, obj):
        """add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current database session"""
        if obj:
            self.__session.query(obj).all().delete()


    det reload(self):
        """create all tables in the database"""
        Session = scoped_session(sessionmaker(bind=engine, expire_on_commit=false))
        self.__session = Session()
