from pydantic import BaseModel, Field
from uuid import UUID
from app.db import get_db 
class DatabaseRequest(BaseModel):
    event_id: UUID
    event_type: str
    payload: dict 
