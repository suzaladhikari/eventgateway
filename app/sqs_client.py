import boto3 
import json 
import os 

sqs = boto3.client("sqs", region_name = os.getenv('AWS_REGION'))
