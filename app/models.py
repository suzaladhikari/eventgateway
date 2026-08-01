from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class EventGateWay(Base): ## Setting up the blueprint 
    __tablename__ = 'events' ## The table name that stores the value is called events 
    event_id = Column(Integer, primary_key=True)
        


