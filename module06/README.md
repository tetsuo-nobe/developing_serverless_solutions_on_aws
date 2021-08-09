
## モジュール6のデモ/サンプル


### AWS Lambda × Amazon SQS

- sqsフォルダ
  - Demo-SQS-FunctionA.py
  - Demo-SQS-FunctionB.py
  - Demo-SQS-FunctionC.py
    - これらのLambda関数は、基本的に全て処理内容は同じで、それぞれトリガーで設定されたSQSのQueueへポーリングして取得したメッセージを表示する。
    - ただし、メッセージ内容が "abort" だった場合は強制的にエラーを発生させている。


  ### AWS Lambda × Amazon Kinesis
- kinesisフォルダ
  - Demo-Kinesis-PublishData-FunctionC.py
    - Kinesis ストリームにレコードを20件Putする。
  - Demo-Kinesis-FunctionC.py
    - Kinesis ストリームにポーリングして取得したレコードを表示する。
    






