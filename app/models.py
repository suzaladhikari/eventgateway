from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class EventGateWay(Base): ## Setting up the blueprint 
    __tablename__ = 'events' ## The table name that stores the value is called events 
    def __init__(self,event_id, event_type, payload, status, received_at, processed_at, retry_count):
        self.event_id = Column(event_id, primary_key=True)
        


