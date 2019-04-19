import json
import boto3

dynamodb = boto3.resource('dynamodb')

def list_responses(event, context):
    table = dynamodb.Table('Application_migration_responses')

    # fetch all ApplicationMigration from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }

    return response

