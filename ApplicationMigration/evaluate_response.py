import json
import boto3

dynamodb = boto3.resource('dynamodb')


def evaluate_response(event, context):
    table = dynamodb.Table('Application_migration_responses')

    # fetch all ApplicationMigration from the database
    key = {'app_name': event.path_params['app_name']}
    form_response = table.get_item(Key=key)
    form_response = json.dumps(form_response)
    warning = []
    error = []
    if form_response['programming_language'] != 'java':
        warning.append("Currently, Java applications are primarily supported.")
    if form_response['maven_dependencies'] != 'Yes':
        error.append("Your application should utilize Maven for dependency management to be cloud ready.")
    if form_response['maven_build'] != 'Yes':
        error.append("Your application should utilize Maven for build automation to be cloud ready.")
    if form_response['jenkins'] != 'Yes':
        warning.append("Your application should utilize Jenkins for build automation to be cloud ready, \
        but we can help you build a Jenkins instance in the following steps.")
    if form_response['artifactory'] != 'Yes':
        error.append("Your application should utilize Artifactory for release management to be cloud ready.")
    if form_response['tomcat'] != 'Yes':
        error.append("Applications need to remove dependencies from IBM web-sphere and utilize Tomcat.")
    if form_response['Authentication'] != 'Yes':
        error.append("Consider re-evaluating your applications authentication practices.")
    if form_response['message_driven_beans'] != 'Yes':
        warning.append("Consider using Message Driven Beans instead of plain old java objects.")
    if form_response['jdbc'] != 'Yes':
        error.append("Applications should utilize JDBC templates instead of SQL, \
        as DB2 will not be supported in the cloud.")
    if form_response['rest'] != 'Yes':
        warning.append("SOAP Services need to be changed to REST based services.")
    if form_response['elk'] != 'Yes':
        error.append("Disable SOARTM in favor of using an ELK solution.")
    if form_response['centralized_logs'] != 'Yes':
        error.append("Applications need to consider writing logs to a centralized logging system.")
    if form_response['file_system'] != 'Yes':
        warning.append("Applications need to consider writing files to other storage options, like S3.")
    if form_response['communication'] != 'Yes':
        warning.append("Applications that communicate excessively with \
        on-premise resources could experience delays in the cloud.")
    if form_response['database'] == 'Oracle':
        warning.append('Currently, Oracle is supported but could incur higher costs.')
    if form_response['database'] == "DB2":
        error.append("DB2 is not currently supported in the cloud")

    # create a response
    response = {
        "statusCode": 200,
        "body": {
            "warning": warning,
            "error": error
        }
    }

    return response

