import json
import boto3

def lambda_handler(event, context):
    # メッセージをすべてprint
    print("--- START Demo FailResponse Function ---")
    i = 0
    failItems = []
    for record in event['Records']:
       i+=1
       print("No="+str(i))
       payload=record["body"]
       print(payload)
       # 内容が 'abort'の場合は処理失敗とする
       if payload == 'abort':
         msg_id=record["messageId"]
         failItems.append({"itemIdentifier": msg_id})    
         
    # 失敗したメッセージIDを報告(return)
    failResponse = { 
        "batchItemFailures": failItems
    }
    return failResponse
