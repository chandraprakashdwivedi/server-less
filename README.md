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

#serverless create -t azure-python3 --path <my-service>    //For Azure
  
#cd my-service

Deploy a Service:
Use this when you have made changes to your Functions, Events or Resources in serverless.yml or you simply want to deploy all changes within your Service at the same time.

#serverless deploy -v

Deploy the Function:
Use this to quickly upload and overwrite your AWS Lambda code on AWS, allowing you to develop faster.

#serverless deploy function -f hello

Invoke the Function:
Invokes an AWS Lambda Function on AWS and returns logs.

#serverless invoke -f hello -l

Fetch the Function Logs:
Open up a separate tab in your console and stream all logs for a specific Function using this command.

#serverless logs -f hello -t

Remove the Service:
Removes all Functions, Events and Resources from your AWS account.

#serverless remove

How to Install a Service:
This is a convenience method to install a pre-made Serverless Service locally by downloading the Github repo and unzipping it. Services are listed below.

#serverless install -u https://github.com/your-url-to-the-serverless-service

Check out the Serverless Framework Guide for more information.
