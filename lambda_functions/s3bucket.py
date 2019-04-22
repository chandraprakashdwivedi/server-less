import json
import boto3

s3 = boto3.resource('s3')

def s3list(event,context):
    my_bucket = s3.Bucket('test-sls-dev-uploads')
    bucket_obj = []
    
    for object in my_bucket.objects.all():
        print(object, object.bucket_name)
        bucket_obj.append(object.key)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(bucket_obj)
        
    }

    return response
    
    
