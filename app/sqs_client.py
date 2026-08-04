import boto3 
print(boto3.__version__)
import json 
import os 

sqs = boto3.client("sqs", region_name = os.getenv('AWS_REGION')) ## Setting up the sqs service for client 

def send_event_to_queue(event_data: dict):
    response = sqs.send_message(
        QueueUrl = os.getenv('SQS_QUEUE_URL'), ## Using the url for dropping the request 
        MessageBody = json.dumps(event_data)
    )
    return response 
