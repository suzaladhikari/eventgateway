### This is where we actually connect the python app to postgres 
from sqlalchemy import create_engine
DATABASE_URL = create_engine('postgresql://admin:password@localhost:5432/mydatabase')
engine = create_engine(DATABASE_URL) ## Connecting to the local database 
