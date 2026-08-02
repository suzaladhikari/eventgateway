from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from enum import Enum
from datetime import datetime, timezone
class DatabaseRequest(BaseModel):
    event_id: UUID
    event_type: str
    payload: dict 
