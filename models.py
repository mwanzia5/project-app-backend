from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Text,VARCHAR,Integer,DateTime,TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Cake(Base):
    __tablename__ = "cakes"

    id = Column(Integer, primary_key=True)
    type = Column(Text(),nullable=False)
    description = Column(VARCHAR,nullable=False)
    image = Column(VARCHAR,nullable=False)
    size = Column(Integer,nullable=False)
    price = Column(Integer,nullable=False)
    date = Column(DateTime,nullable=False)
    created_at = Column(TIMESTAMP)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    phone = Column(VARCHAR, nullable=False, unique=True)

    bookings = relationship("Booking", backref="user")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer(), primary_key=True)
    booking_date = Column(DateTime(), nullable=False)


    cake_id = Column(Integer(), ForeignKey('cakes.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))


