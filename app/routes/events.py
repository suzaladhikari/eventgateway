### Here users will post the request
from fastapi import APIRouter, Depends
from app.models import Event 
from app.schemas import DatabaseRequest
from sqlalchemy.orm import Session
from app.db import get_db
from app.sqs_client import send_event_to_queue
router = APIRouter()

@router.post('/events', status_code=202) ## Event received and processing started
def create_events(request: DatabaseRequest):
## Db creates a seesion that makes sure that the connection is made to the database once the request is made
    new_event = Event(
        event_id = request.event_id,
        event_type = request.event_type,
        payload = request.payload
    )
    send_event_to_queue(new_event)
    return {"status":"accepted", "event_id":new_event.event_id}
