from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Text,VARCHAR,Integer,DateTime,TIMESTAMP

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


