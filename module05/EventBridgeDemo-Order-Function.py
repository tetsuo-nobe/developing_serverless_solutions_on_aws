import json
import boto3
import datetime
from aws_xray_sdk.core import patch
patch(['boto3'])

def lambda_handler(event, context):
    #
    order = event["order"]
    client = boto3.client('events')
    # 
    client.put_events(
        Entries=[{
            "Time": datetime.datetime.now(),
            "Source": "demo.eventbridge.order",
            "DetailType": "OrderCreated",
            "Resources": [
               order["orderId"]
            ],
            "Detail": json.dumps(order),
            "EventBusName": "EventBridgeDemo-bus"
        }]
    )
    #
    return {
        'statusCode': 200,
        'body': json.dumps('** The order event was issued **')
    }
