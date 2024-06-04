import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    icon = Column(String(250), nullable=False)
    comments = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer,ForeignKey('post.id'))
    post = relationship(Post)

class Reactions(Base):
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key=True)
    number_of_likes = Column(Integer, nullable=False)
    number_of_dislikes = Column(Integer, nullable=False)
    post_id = Column(Integer,ForeignKey('post.id'))
    post = relationship(Post)
    comment_id = Column(Integer,ForeignKey('comments.id'))
    comment = relationship(Comments)




# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
