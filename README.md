# Serverless (https://serverless.com/)

## Some quick hands on youtube videos

https://youtu.be/x1S8MLVZV44

Channel https://youtu.be/lUTGk64jppM?list=PLzvRQMJ9HDiT5b4OsmIBiMbsPjfp4kfg3

git repo https://github.com/serverless/serverless

This repository performs automation using a new tool named serverless by defination it say code one and run on any cloud, similar as like terraform.

Installation Steps:

https://serverless.com/framework/docs/providers/aws/guide/installation/

Supporting Platforms:

It is supporting all the public clouds.

https://serverless.com/framework/docs/providers/

Authorization Step:

For authorization use the same concept of creating .aws in the root directory.

## Steps to create project

Create a Service:

#serverless create --template aws-python3 --path <my-service>   //For AWS

#serverless create -template azure-python3 --path <my-service>    //For Azure
  
#cd my-service

Deploy a Service: \
Use this when you have made changes to your Functions, Events or Resources in serverless.yml or you simply want to deploy all changes within your Service at the same time.

#serverless deploy --stage prod --region ap-south-1

Deploy the Function: \
Use this to quickly upload and overwrite your AWS Lambda code on AWS, allowing you to develop faster.

#serverless deploy function -f hello

Invoke the Function: \
Invokes an AWS Lambda Function on AWS and returns logs.

#serverless invoke -f hello -l

Fetch the Function Logs:
Open up a separate tab in your console and stream all logs for a specific Function using this command.

#serverless logs -f hello -t

Remove the Service: 
Removes all Functions, Events and Resources from your AWS account.

#serverless remove 

How to Install a Service: <br/>
This is a convenience method to install a pre-made Serverless Service locally by downloading the Github repo and unzipping it. Services are listed below.

#serverless install -u https://github.com/your-url-to-the-serverless-service

Check out the Serverless Framework Guide for more information.

Some Notes: \

### Every serverless.yml translates to a single AWS CloudFormation template and a CloudFormation stack is created from that resulting CloudFormation template.

handler.js: \
The handler.js file contains your function code. The function definition in serverless.yml will point to this handler.js file and the function exported here.

event.json: \
Note: This file is not created by default

Create this file and add event data so you can invoke your function with the data via 

#serverless invoke -p event.json

Deployment: \
When you deploy a Service, all of the Functions, Events and Resources in your serverless.yml are translated to an AWS CloudFormation template and deployed as a single CloudFormation stack.

Note: Deployment defaults to dev stage and us-east-1 region on AWS, unless you specified these elsewhere, or add them in as options:

#serverless deploy --stage prod --region us-east-1

Removal:
To easily remove your Service from your AWS account, you can use the remove command.

#serverless remove -v

Pinning a Version: \ 
To configure version pinning define a frameworkVersion property in your serverless.yaml. Whenever you run a Serverless command from the CLI it checks if your current Serverless version is matching the frameworkVersion range

#cat serverless.yml \

frameworkVersion: "=1.0.3" ...

or

frameworkVersion: ">=1.0.0 <2.0.0"

## AWS - Functions: \
If you are using AWS as a provider, all functions inside the service are AWS Lambda functions.

Log Group Resources: \
By default, the framework will create LogGroups for your Lambdas. This makes it easy to clean up your log groups in the case you remove your service, and make the lambda IAM permissions much more specific and secure.

Versioning Deployed Functions: <br\>
By default, the framework creates function versions for every deploy. This behavior is optional, and can be turned off.These versions are not cleaned up by serverless, so make sure you use a plugin or other tool to prune sufficiently old versions. The framework can't clean up versions because it doesn't have information about whether older versions are invoked or not. This feature adds to the number of total stack outputs and resources because a function version is a separate resource from the function it refers to.

provider: <br\>
  versionFunctions: false
  
Dead Letter Queue (DLQ): 
When AWS lambda functions fail, they are retried. If the retries also fail, AWS has a feature to send information about the failed request to a SNS topic or SQS queue, called the Dead Letter Queue, which you can use to track and diagnose and react to lambda failures.You can setup a dead letter queue for your serverless functions with the help of a SNS topic and the onError config parameter.

Note: You can only provide one onError config per function.

functions:
  hello:
    handler: handler.hello
    onError: arn:aws:sns:us-east-1:XXXXXX:test # Ref, Fn::GetAtt and Fn::ImportValue are supported as well
    
KMS Keys:
AWS Lambda uses AWS Key Management Service (KMS) to encrypt your environment variables at rest.

service:
  name: service-name
  awsKmsKeyArn: arn:aws:kms:us-east-1:XXXXXX:key/some-hash

provider:
  name: aws
  environment:
    TABLE_NAME: tableName1

functions:
  hello: # this function will OVERWRITE the service level environment config above
    handler: handler.hello
    awsKmsKeyArn: arn:aws:kms:us-east-1:XXXXXX:key/some-hash
 
## AWS - Events
Events are the things that trigger your functions to run like an S3 bucket upload, an SNS topic, and HTTP endpoints created via API Gateway.

## AWS CloudFormation Resource Reference: \
To have consistent naming in the CloudFormation Templates that get deployed we use a standard pattern:

{Function Name}{Cloud Formation Resource Type}{Resource Name}{SequentialID, instanceId or Random String}

Function Name - This is optional for Resources that should be recreated when the function name gets changed. Those resources are also called function bound
Cloud Formation Resource Type - E.g., S3Bucket
Resource Name - An identifier for the specific resource, e.g. for an S3 Bucket the configured bucket name.
SequentialID, instanceId or Random String - For a few resources we need to add an optional sequential id, the Serverless instanceId (accessible via ${sls:instanceId}) or a random string to identify them.

All resource names that are deployed by Serverless have to follow this naming scheme. 

Number of resources deployed using serverless in AWS
https://serverless.com/framework/docs/providers/aws/guide/resources/

Events can be triggered by AWS Lambda on these services

https://serverless.com/framework/docs/providers/aws/events/

## AWS Resource Template url reference

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html



  






