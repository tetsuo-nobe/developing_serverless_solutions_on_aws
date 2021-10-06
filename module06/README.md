
## モジュール6のデモ/サンプル


### AWS Lambda × Amazon SQS

- sqsフォルダ
  - Demo-SQS-Function.py
    - SQSキューをイベントソースに設定したLambda関数の例
  - Demo-SQS-SDK.py
    - SQSキューからメッセージを受診するAWS SDKのコードの例
  - 上記いずれもサンプルで、エラー処理などは割愛しています。
  - また、メッセージの取り出され方はSDKとLambdaでは異なります。

### AWS Lambda × DynamoDB Stream
- dynamodb-streamフォルダ
  - Demo-DynamoDB-Stream-Function.py
    - DynamoDB Streamから取得したデータを表示する


### AWS Lambda × Amazon Kinesis
- kinesisフォルダ
  - Demo-Kinesis-PublishData-FunctionC.py
    - Kinesis ストリームにレコードを20件Putする。
  - Demo-Kinesis-FunctionC.py
    - Kinesis ストリームにポーリングして取得したレコードを表示する。
    






