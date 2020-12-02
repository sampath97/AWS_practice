import boto3
import csv

#read credentials from csv
with open('aws_credentials.csv','r') as input:
    next(input)
    data=csv.reader(input)
    for line in data:
        access_id=line[2]
        secret_access_key=line[3]


#read image from csv
with open('Images/quote1.jpg','rb') as image:
    img_bytes=image.read()

#create aws client
aws_client=boto3.client('rekognition',region_name='ap-south-1',aws_secret_access_key=secret_access_key,aws_access_key_id=access_id)

result=aws_client.detect_text(Image={'Bytes':img_bytes})

final_text=''

#parse through the response to get the combined text

for key,value in result.items():
    if key=='TextDetections':
        for i in range(0,len(value)-1):
            if value[i]['Type'] == 'LINE':
                final_text=final_text+' '+value[i]['DetectedText']

        print('exiting from for loop')
        break       

print(final_text)