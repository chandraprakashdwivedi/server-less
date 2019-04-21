import json
import boto3

s3 = boto3.resource('s3')

def s3list(event,context):
    my_bucket = s3.Bucket('test-sls-dev-uploads')
    
    for object in my_bucket.objects.all():
        print(object)
    
    response = {
        "statusCode": 200
    }

    return response
    
    
