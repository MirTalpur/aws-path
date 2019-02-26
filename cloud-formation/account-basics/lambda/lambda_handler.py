# Takes in the UserName of the IAM User
# Uses boto3 to create_access_keys
# Stores those access_keys in a S3 Bucket
import boto3

def handler(event, context):
  print(event)
  user_name = event['user_name']
  # client = boto3.client('iam')
  # response = client.create_access_keys(
  #   UserName=user_name
  # )
  # client = boto3.client('s3')
  # s3_response = client.create_bucket(
  #   ACL='authenticated-read'
  #   Bucket='lambda-hskalee123-bucket-s3-user'
  # )

if __name__ == "__main__":
  class Event:
    def __getitem__(self, key):
      e = {
        'user_name': 'value1'
      }
      return e[key]
  context = 'context'
  event = Event()
  print(handler(event, context))
