def lambda_handler(event, context):
    # メッセージをすべてprint
    for record in event['Records']:
       payload=record['body']
       print(str(payload))
