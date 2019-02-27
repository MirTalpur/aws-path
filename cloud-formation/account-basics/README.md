# AWS-Path: Automation
# Account Basics

### Goal
We will create IAM users through the UI and than automate the process except for the access key and secret keys (we will see why
we won't be automating those two user information)

Note: In order to know what to automate it's better to do it manually first and than you have a better understanding of what
you will be automating.

Start with Creating an IAM User and access and secret keys

Go to cloudformation apply:
user-group.yaml
and than
user.yaml

Problem occured when trying to create a lambda function which creates the access_keys and secrets_keys and stores them into S3.
In order to create the lambda function which requires boto3 to store objects in S3 we need access_keys and secret_keys which leads to a circular dependency and the chicken and the egg question. Just creating the IAM user and UserGroup using cloudformation is enough automation for IAM for now.

Creating the access_keys and secret_keys via cloudformation leads and outputting them to cloudformation outputs leads to a secruity vulnerabilites which we don't want.
