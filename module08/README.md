
## モジュール8のデモ/サンプル


### AWSサービス(他のステートマシン）の待機
- syncフォルダ
  - Nest-Child-StateMachine.json
    - Parentから呼び出されるステートマシン
  - Nest-Parent-StateMachine.json
    - Chileを呼出して完了を待機する

### waitForTaskTokenの使用
- waitForTaskToken_Basicフォルダ
  - Demo-sfn-waitForTaskToken-Function.js
    - ステートマシンにタスクトークンを返すLambda関数
  - Demo-sfn-waitForTaskToken.json
    - SQSキューにメッセージを送信し、Lambda関数からのタスクトークンを待機するステートマシン

- waitForTaskToken_VacationRequestフォルダ
  - Demo-sfn-waitForTaskToken-Function.js
    - 休暇申請を承認して、ステートマシンにタスクトークンを返すLambda関数
  - Demo-Vaction-Request-StateMachine.json
    - 休暇申請を受付てSQSキューにメッセージを送信し、Lambda関数からのタスクトークンを待機するステートマシン
    - 申請の情報や、承認、却下の情報をDynamoDBで管理する
  - このサンプルも、Workflow Studioだけで作成(Lambda関数を使っていない）

### Workflow Studioだけで作成した(Lambda関数を使わない）画像認識サービス
- workflowStudioフォルダ
  - Demo-Image-Rekognition-StateMachine.json
    - S3バケットに格納された画像をAmazon Rekognitionでラベル検出してDynamoDBに格納するステートマシン
    - S3で発生したイベントは直接EventBridgeに渡され、EventBridgeによりステートマシンが起動






