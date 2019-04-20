import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table('Application_migration_responses')

    table.delete_item(
        Key={
            'app_name': event['pathParameters']['app_name']
        }
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
