from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
import uuid
Base = declarative_base()
class EventGateWay(Base): ## Setting up the blueprint 
    __tablename__ = 'events' ## The table name that stores the value is called events 
    event_id = Column(UUID(as_uuid=True),default=uuid.uuid4, primary_key=True) ## This is the unique eventId
    event_type = Column(String, nullable=False) # What type of event is it ?!
    payload = Column(JSONB, nullable=False) ## Accepts the json format 
    status = Column(Enum('pending', 'processing', 'completed', 'failed', name = 'event_status'), nullable= False, default='pending' ) ## What is the status
    received_at = Column(DateTime(timezone=True), server_default=func.now())
    processed_at = Column(DateTime(timezone=True), nullable=True)
    retry_count = Column(Integer, nullable=False, default=0)

        


