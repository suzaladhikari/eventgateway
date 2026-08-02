### Here users will post the request
from fastapi import APIRouter
from app.schemas import DatabaseRequest
router = APIRouter()

@router.post('/events', status_code=202) ## Event received and processing started
def events(request: DatabaseRequest):
    return "You have made it to this point"
