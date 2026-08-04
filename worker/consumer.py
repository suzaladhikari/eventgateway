## To view the sqs !
## Go to the aws console as a IAM user as well: user id : 8716-4028-5396
import boto3
import os 
from dotenv import load_dotenv
import json 
load_dotenv()
sqs = boto3.client("sqs", region_name = os.getenv('AWS_REGION'))
response = sqs.receive_message(QueueUrl = os.getenv("SQS_QUEUE_URL"))
dlq = sqs.receive_message(QueueUrl = os.getenv("DLQ_URL"))

