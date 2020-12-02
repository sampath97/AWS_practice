import boto3
import cv2
import csv

with open('aws_credentials.csv','r') as input:
    next(input)
    data=csv.reader(input)
    for line in data:
        aws_access_id=line[2]
        aws_secret_access_key=line[3]
    
with open('Images/beach_family2.jpg','rb') as image:
    img_bytes=image.read()

aws_client=boto3.client('rekognition',region_name='ap-south-1',aws_access_key_id=aws_access_id,aws_secret_access_key=aws_secret_access_key)

result=aws_client.detect_moderation_labels(Image={'Bytes':img_bytes})

print(result)