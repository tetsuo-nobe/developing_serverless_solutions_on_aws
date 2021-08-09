import boto3
import json
import time
import ast

def lambda_handler(event, context):
    # TODO implement
    kinesis = boto3.client("kinesis")

    for id in range(1,21):
        strData =  "{'id':'" + str(id) + "','timestamp_ms':'"+ str(id) + "', 'text': 'data"+ str(id) + "'}" 
        dictData = ast.literal_eval(strData)
        #time.sleep(1)
        kinesis.put_record(StreamName="demo-kinesis-stream", Data=json.dumps(dictData), PartitionKey=dictData['timestamp_ms'])
    return {
        'statusCode': 200,
        'body': json.dumps('Published!')
    }
