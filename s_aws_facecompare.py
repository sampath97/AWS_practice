import boto3
import csv

#read credentials from csv
with open('aws_credentials.csv','r') as input:
    next(input)
    data=csv.reader(input)
    for line in data:
        access_id=line[2]
        secret_access_key=line[3]


#read source image from folder
with open('Images/fav.jpg','rb') as image:
    src_img_bytes=image.read()

#read target image from folder
with open('Images/friends.jpg','rb') as image:
    target_img_bytes=image.read()    

#create aws client
aws_client=boto3.client('rekognition',region_name='ap-south-1',aws_secret_access_key=secret_access_key,aws_access_key_id=access_id)

result=aws_client.compare_faces(SourceImage={'Bytes':src_img_bytes},TargetImage={'Bytes':target_img_bytes})

for key,value in result.items():
    if key in {'FaceMatches'}:
        #get the bounding bix values of matched face
        print(result['FaceMatches'][0]['Face']['BoundingBox']['Width'])
        print(result['FaceMatches'][0]['Face']['BoundingBox']['Height'])
        print(result['FaceMatches'][0]['Face']['BoundingBox']['Left'])
        print(result['FaceMatches'][0]['Face']['BoundingBox']['Top'])
        
                




