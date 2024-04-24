import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    email = Column(String(180), nullable=False)
    password = Column(String(180), nullable=False)
    subscription_date = Column(String(180))

    
class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column (Integer)
    diameter = Column (Integer)
    gravity = Column (Integer)
    # favorite_id = Column(Integer, ForeignKey('favorite.id'))
    # favorite = relationship(Favorite)

    
class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column (Integer)
    hair_color = Column(String(180))
    # character_favorite = Column(Integer, ForeignKey("favorite.id"))
    # character = relationship(Favorite)


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
