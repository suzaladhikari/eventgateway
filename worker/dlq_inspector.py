import boto3, os, json
from dotenv import load_dotenv
load_dotenv()

sqs = boto3.client("sqs", region_name = os.getenv("AWS_REGION"))
DLQ_URL = os.getenv("DLQ_URL")

response = sqs.receive_message(QueueUrl = DLQ_URL, MaxNumberOfMessages = 10, WaitTimeSeconds = 5)
