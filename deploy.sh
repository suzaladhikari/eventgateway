set -e 
REGION=us-east-1 ## Setting up the region 
ACCOUNT_ID=871640285396 ## Setting up the account_id for IAM user 
aws ecr get-login-password --region $REGION docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com ## This is how the docker logs in to the aws 

### Producer 
docker build -f Dockerfile.fastapi -t eventgateway-producer . ## Building the docker image from the dockerfile
docker tag eventgateway-producer:latest $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/eventgateway-producer:latest ## Naming the image
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/eventgateway-producer:latest
