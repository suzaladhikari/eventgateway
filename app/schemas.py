from pydantic import BaseModel, Field
from uuid import UUID
class DatabaseRequest(BaseModel):
    event_id: UUID
    event_type: str
    payload: dict 
