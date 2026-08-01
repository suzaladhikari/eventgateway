from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
Base = declarative_base()
class EventGateWay(Base): ## Setting up the blueprint 
    __tablename__ = 'events' ## The table name that stores the value is called events 
    event_id = Column(UUID(as_uuid=True),default=uuid.uuid4, primary_key=True) ## This is the unique eventId
    event_type = Column(String, nullable=False) # What type of event is it ?!
    payload = Column(JSONB, nullable=False) ## Accepts the json format 
    status = Column(Enum('pending', 'processing', 'completed', 'failed', name = 'event_status'), nullable= False, default='pending' )
    

        


