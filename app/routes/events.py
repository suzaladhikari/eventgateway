### Here users will post the request
from fastapi import APIRouter, Depends
from app.schemas import DatabaseRequest
from app.models import Event 
from app.schemas import DatabaseRequest
from app.db import get_db

router = APIRouter()

@router.post('/events', status_code=202) ## Event received and processing started
def events(request: DatabaseRequest):
    return "You have made it to this point"
