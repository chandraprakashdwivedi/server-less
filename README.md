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

Remove the Service: \
Removes all Functions, Events and Resources from your AWS account.

#serverless remove

How to Install a Service: \ 
This is a convenience method to install a pre-made Serverless Service locally by downloading the Github repo and unzipping it. Services are listed below.

#serverless install -u https://github.com/your-url-to-the-serverless-service

Check out the Serverless Framework Guide for more information.

Some Notes: \

### Every serverless.yml translates to a single AWS CloudFormation template and a CloudFormation stack is created from that resulting CloudFormation template.

handler.js:\
The handler.js file contains your function code. The function definition in serverless.yml will point to this handler.js file and the function exported here.

event.json: \
Note: This file is not created by default

Create this file and add event data so you can invoke your function with the data via 

#serverless invoke -p event.json

Deployment:\
When you deploy a Service, all of the Functions, Events and Resources in your serverless.yml are translated to an AWS CloudFormation template and deployed as a single CloudFormation stack.

Note: Deployment defaults to dev stage and us-east-1 region on AWS, unless you specified these elsewhere, or add them in as options:

#serverless deploy --stage prod --region us-east-1

Removal:
To easily remove your Service from your AWS account, you can use the remove command.

#serverless remove -v

Pinning a Version:
To configure version pinning define a frameworkVersion property in your serverless.yaml. Whenever you run a Serverless command from the CLI it checks if your current Serverless version is matching the frameworkVersion range

#cat serverless.yml\

frameworkVersion: "=1.0.3" ...

or

frameworkVersion: ">=1.0.0 <2.0.0"





