# Serverless (https://serverless.com/)

git repo https://github.com/serverless/serverless

This repository performs automation using a new tool named serverless by defination it say code one and run on any cloud, similar as like terraform.

Installation Steps:

https://serverless.com/framework/docs/providers/aws/guide/installation/

Supporting Platforms:

It is supporting all the public clouds.

https://serverless.com/framework/docs/providers/

## Steps to create project

Create a Service:

#serverless create --template aws-nodejs --path my-service
#cd my-service

Deploy a Service:
Use this when you have made changes to your Functions, Events or Resources in serverless.yml or you simply want to deploy all changes within your Service at the same time.

#serverless deploy -v

Deploy the Function:
Use this to quickly upload and overwrite your AWS Lambda code on AWS, allowing you to develop faster.

serverless deploy function -f hello
Invoke the Function:
Invokes an AWS Lambda Function on AWS and returns logs.

serverless invoke -f hello -l
Fetch the Function Logs:
Open up a separate tab in your console and stream all logs for a specific Function using this command.

serverless logs -f hello -t
Remove the Service:
Removes all Functions, Events and Resources from your AWS account.

serverless remove
How to Install a Service:
This is a convenience method to install a pre-made Serverless Service locally by downloading the Github repo and unzipping it. Services are listed below.

serverless install -u https://github.com/your-url-to-the-serverless-service
Check out the Serverless Framework Guide for more information.

Services (V1.0)
The following are services you can instantly install and use by running serverless install --url <service-github-url>

serverless-examples
CRUD - CRUD service, Scala Port
CRUD with FaunaDB - CRUD service using FaunaDB
CRUD with S3 - CRUD service using S3
GraphQL Boilerplate - GraphQL application Boilerplate service
Authentication - Authentication boilerplate service
Mailer - Service for sending emails
Kinesis streams - Service to showcase Kinesis stream support
DynamoDB streams - Service to showcase DynamoDB stream support
Landingpage backend - Landingpage backend service to store E-Mail addresses
Facebook Messenger Chatbot - Chatbot for the Facebook Messenger platform
Lambda chaining - Service which chains Lambdas through SNS
Secured API - Service which exposes an API key accessible API
Authorizer - Service that uses API Gateway custom authorizers
Thumbnails - Service that takes an image url and returns a 100x100 thumbnail
Boilerplate - Opinionated boilerplate
ES6 + Jest - ES6 + Jest Boilerplate
PHP - Call a PHP function from your lambda
Ruby - Call a Ruby function from your lambda
Slack App - Slack App Boilerplate with OAuth and Bot actions
Swift - Full-featured project template to develop Lambda functions in Swift
Cloudwatch Alerts on Slack - Get AWS Cloudwatch alerts notifications on Slack


