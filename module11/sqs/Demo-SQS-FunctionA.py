import json
import time

def lambda_handler(event, context):
    # メッセージをすべてprint
    print("--- START Demo SQS Function A---")
    i = 0;
    for record in event['Records']:
       i+=1
       print("No="+str(i))
       payload=record["body"]
       try:
           if payload == "abort":
              zd = 1 / 0
           print(str(payload))
       except Exception as e:
           print(e)
           print('Error getting message')
           raise e

    print("--- END Demo SQS Function A---:処理件数:" + str(i))