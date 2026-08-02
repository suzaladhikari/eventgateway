from pydantic import BaseModel 
from sqlalchemy import Column, Integer, String,Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from enum import Enum

### Only for the event_status
class EventStatus(str, Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    FAILED = 'failed'
    


class DatabaseRequest(BaseModel):
    event_id: UUID
    event_type: str
    payload: dict 
