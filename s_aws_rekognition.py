import csv
import boto3

with open('aws_credentials.csv','r') as input:
    next(input) #take input from next line
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[2] #3rd value is access id
        secret_access_key=line[3] #4th value is secret access key

#convert images to bytes
with open('Images\cricket_ball.png','rb') as source_image:
    img_bytes=source_image.read()

#create boto3 client
aws_client=boto3.client('rekognition', region_name='ap-south-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)

#pass parameters as dictionary
response=aws_client.detect_labels(Image={'Bytes':img_bytes},MaxLabels=5)

print(response)

  