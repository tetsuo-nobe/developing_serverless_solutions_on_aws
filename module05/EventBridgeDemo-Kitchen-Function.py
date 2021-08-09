import json
from aws_xray_sdk.core import patch
patch(['boto3'])

def lambda_handler(event, context):
    # TODO implement
    print("------------------------------------------")
    print(event)
    print("------------------------------------------")
    return {
        'statusCode': 200,
        'body': json.dumps('We have received your meal order.')
    }
