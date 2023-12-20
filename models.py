from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Text,VARCHAR,Integer,TIMESTAMP
base = declarative_base()

class Cake(base):
    __tablename__ ="events"

id = Column(Integer(),primary_key=True)
type = Column(Text())
description =Column(VARCHAR)
image = Column(VARCHAR)
size =Column(Integer())
price = Column(Integer())
date = Column(TIMESTAMP)