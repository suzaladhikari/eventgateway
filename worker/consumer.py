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
from app.models import Event,Base
from app.database import SessionLocal, engine
load_dotenv()
Base.metadata.create_all(bind = engine)
## Creating a database session 
db = SessionLocal()
## Engine to connect sessions to the database

sqs = boto3.client("sqs", region_name = os.getenv('AWS_REGION'))

def poll_and_process():
    db = SessionLocal()
    try:
        response = sqs.receive_message(QueueUrl = os.getenv("SQS_QUEUE_URL"), MaxNumberOfMessages = 10, WaitTimeSeconds = 30)
        for message in response.get('Messages', []):
            try: 
                events = json.loads(message['Body'])
                new_event = Event(event_id = events['event_id'], event_type = events['event_type'], payload = events['payload']) ## This is how the table should be formatted 
                db.add(new_event)
                db.commit()
                sqs.delete_message(QueueUrl = os.getenv("SQS_QUEUE_URL"), ReceiptHandle = message["ReceiptHandle"])
                print("Deleted from SQS")
            except Exception as e:
                db.rollback()
                print("Error", e)
    finally: 
        db.close()

if __name__ == '__main__':
    while True: 
        poll_and_process()
        

