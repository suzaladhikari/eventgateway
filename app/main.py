## Creating the fastapi app 
from fastapi import FastAPI
from app.routes.events import router as events_router

app = FastAPI(title = 'Event GateWay')
app.include_router(events_router)
