import json
import boto3

s3 = boto3.client('s3')


def s3list(event,context):
   data = s3.list_buckets()
   buckets = [bucket['Name'] for bucket in data['Buckets']]
   print("Bucket List: %s" % buckets)

    response = {
        "statusCode": 200
    }

    return response
    
    
