import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='Demo-SQS-SDK-Queue')  
    
# メッセージを受信
msg_list = queue.receive_messages(
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20) 
if msg_list:
   for message in msg_list:
     print(message.body)         
     # メッセージを削除
     message.delete()