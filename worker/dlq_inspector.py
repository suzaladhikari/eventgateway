import boto3, os, json
from dotenv import load_dotenv
load_dotenv()

sqs = boto3.client("sqs", region_name = os.getenv("AWS_REGION"))
DLQ_URL = os.getenv("DLQ_URL")

while True: 
    response = sqs.receive_message(QueueUrl = DLQ_URL, MaxNumberOfMessages = 10, WaitTimeSeconds = 5)
    messages = response.get('Messages', [])
    if not messages: 
        break
    for message in messages:
        body = json.loads(message['Body'])
        print(body.get('event_id'))