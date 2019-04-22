import json
import boto3

s3 = boto3.resource('s3')

def s3list(event,context):
    print('event', event)
    my_bucket = s3.Bucket('test-sls-dev-uploads')
    bucket_obj = []
    
    for object in my_bucket.objects.all():
        print(object, object.bucket_name)
        bucket_obj.append(object.key)
        
    sns = boto3.client('sns')
    response = sns.publish(
     TopicArn='arn:aws:sns:ap-south-1:015878554706:test-sls-dev-topic',
     Message=json.dumps({'default': json.dumps(bucket_obj)}),
     Subject='your s3 bucket items',
     MessageStructure='json'
    )
    
    response = {
        "statusCode": 200,
        "body": json.dumps(bucket_obj)
        
    }

    return response
    
    
