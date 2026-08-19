### This is where we actually connect the python app to postgres 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

engine = create_engine(DATABASE_URL) ## Connecting to the local database 
SessionLocal = sessionmaker(bind = engine) ## Creating session 

def get_db():
    db = SessionLocal() ## This can interact with postgres database through the created session
    try:
        yield db 
    finally: 
        db.close()
