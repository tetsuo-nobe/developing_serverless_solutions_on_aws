import json
import time
import boto3

sqs_client = boto3.client("sqs")
queue_url = "https://sqs.ap-northeast-1.amazonaws.com/000000000000/DemoQueueD"

def lambda_handler(event, context):
    # メッセージをすべてprint
    print("--- START Demo SQS Function D---")
    i = 0;
    for record in event['Records']:
       i+=1
       print("No="+str(i))
       payload=record["body"]
       try:
           if payload == "abort":
              zd = 1 / 0
           print(str(payload))
           #
           print('--- delete_message ---')
           receipt_handle=record["receiptHandle"]
           sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
       except Exception as e:
           print(e)
           print('Error getting message')
           raise e

    print("--- END Demo SQS Function D---")