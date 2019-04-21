import json
import boto3

def s3list(event,context):
    bucket = conn.get_bucket('test-sls-dev-uploads', validate=False)
    print(bucket)
    for key in bucket.list(prefix='test-sls-dev-uploads'):
        print("Bucket List: %s" % key)

    response = {
        "statusCode": 200
    }

    return response
    
    
