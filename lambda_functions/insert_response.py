import json
import boto3

dynamodb = boto3.resource('dynamodb')

def insert(event, context):
    table = dynamodb.Table('Application_migration_responses')
    if 'body' in event and event['body'] is not None:
        body = json.loads(event['body'])
    item = {
        "account": body['account'],
        "org": body['org_unit'],
        "app_name": body['app_name'],
        "programming_language": body['programming_language'],
        "maven_dependencies": body['maven_dependencies'],
        "maven_build": body['maven_build'],
        "jenkins": body['jenkins'],
        "artifactory": body['artifactory'],
        "tomcat": body['tomcat'],
        "authentication": body['authentication'],
        "message_driven_beans": body['message_driven_beans'],
        "jdbc": body['jdbc'],
        "rest": body['rest'],
        "elk": body['elk'],
        "centralized_logs": body['centralized_logs'],
        "database": body['database'],
        "file_system": body['file_system'],
        "communication": body['communication']
    }
    table.put(item)
    # create a response
    response = {
        "statusCode": 200,
        "body": "Item Inserted successfully"
    }
    return response
