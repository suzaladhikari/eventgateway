## To view the sqs !
## Go to the aws console as a IAM user as well: user id : 8716-4028-5396
import boto3
import os 
import sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
from dotenv import load_dotenv
import json 
from app.models import Event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
load_dotenv()

## Engine to connect sessions to the database
engine = create_engine(os.getenv("RDS_DATABASE"))
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
sqs = boto3.client("sqs", region_name = os.getenv('AWS_REGION'))
response = sqs.receive_message(QueueUrl = os.getenv("SQS_QUEUE_URL"), MaxNumberOfMessages = 1, WaitTimeSeconds = 10)
for message in response.get('Messages', []):
    try: 
        events = json.loads(message['Body'])
    
        

