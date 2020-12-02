import boto3
import csv

#read data from csv
with open('aws_credentials.csv','r') as input:
    next(input)
    data=csv.reader(input)
    for line in data:
        aws_acess_id=line[2]
        aws_secret_key=line[3]

#read image in bytes
with open('Images/fav.jpg','rb') as image:
    img_bytes=image.read()    


#create aws client
aws_client=boto3.client('rekognition',region_name='ap-south-1',aws_secret_access_key=aws_secret_key,aws_access_key_id=aws_acess_id)

#detect face attributes
result=aws_client.detect_faces(Image={'Bytes':img_bytes},Attributes=['ALL'])

print(result)