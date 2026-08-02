from pydantic import BaseModel 
from sqlalchemy import Column, Integer, String,Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB

class DatabaseRequest(BaseModel):
    event_id: UUID
    event_type: str
    payload: dict 