### Here users will post the request
from fastapi import APIRouter, Depends
from app.models import Event 
from app.schemas import DatabaseRequest
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter()

@router.post('/events', status_code=202) ## Event received and processing started
def create_events(request: DatabaseRequest, db: Session = Depends(get_db)):
    new_event = Event(
        event_id = request.event_id,
        event_type = request.event_type,
        payload = request.payload
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"status":"accepted", "event_id":new_event.event_id}
