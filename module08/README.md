
## モジュール8のデモ/サンプル


### AWSサービス(他のステートマシン）の待機
- syncフォルダ
  - Nest-Child-StateMachine.json
    - Parentから呼び出されるステートマシン
  - Nest-Parent-StateMachine.json
    - Chileを呼出して完了を待機する

### waitForTaskTokenの使用
- waitForTaskTokenフォルダ
  - Demo-sfn-waitForTaskToken-Function.py
    - ステートマシンにタスクトークンを返すLambda関数
  - Demo-sfn-waitForTaskToken.json
    - SQSキューにメッセージを送信し、Lambda関数からのタスクトークンを待機するステートマシン





