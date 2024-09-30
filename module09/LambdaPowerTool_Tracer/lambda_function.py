import os

import boto3
import random
from boto3.dynamodb.types import TypeDeserializer

## PowerTool Tracer をインポート
from aws_lambda_powertools import Tracer
tracer = Tracer(service="jam-service")

table_name = os.environ["TABLE_NAME"]
client = boto3.client("dynamodb")

# @tracer.capture_method デコレーターをつけて関数をサブセグメントとしてトレース出力
@tracer.capture_method
def get_user(id):
    key_name = "id"
    # メタデータの追加
    tracer.put_metadata(key="key_name", value=key_name)
    response = client.get_item(TableName=table_name, Key={key_name: {"S": id}})
    return response["Item"]


def deserialise(item):
    d = TypeDeserializer()
    return {k: d.deserialize(v) for k, v in item.items()}


# @tracer.capture_lambda_handlerデコレーターをつけてハンドラー関数をサブセグメントとしてトレース出力
@tracer.capture_lambda_handler
def handler(event, context):
    user_id = "jammer"
    
    # メタデータの追加
    tracer.put_metadata(key="user_id", value=user_id)
    item = get_user(user_id)
    user = deserialise(item)
    
    # アノテーションの追加
    tracer.put_annotation(key="GetUserStatus", value="SUCCESS")
    
    # サブセグメントの追加
    with tracer.provider.in_subsegment("## assign_group") as subsegment:
        range = 10
        group_id  = random.randrange(range) +1
        subsegment.put_annotation(key="range", value=range)
        subsegment.put_metadata(key="group_id", value=group_id)
        user["group_id"] = group_id
        
    return user
    
