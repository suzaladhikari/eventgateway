import boto3, os, json
from dotenv import load_dotenv
load_dotenv()

sqs = boto3.client("sqs", region_name = os.getenv("AWS_REGION"))
DLQ_URL = os.getenv("DLQ_URL")