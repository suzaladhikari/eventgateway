## To view the sqs !
## Go to the aws console as a IAM user as well: user id : 8716-4028-5396
import boto3
import os 

sqs = boto3.client("sqs", region_name = os.getenv('AWS_REGION'))
