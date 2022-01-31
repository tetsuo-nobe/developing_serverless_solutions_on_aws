
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
    - パラメータは下記
    ```
    {
      "Name": "Nobe"
    }
    ```
  - Demo-sfn-waitForTaskToken.json
    - SQSキューにメッセージを送信し、Lambda関数からのタスクトークンを待機するステートマシン

- waitForTaskToken_VacationRequestフォルダ
  - Demo-sfn-waitForTaskToken-Function.js
    - 休暇申請を承認して、ステートマシンにタスクトークンを返すLambda関数
  
    ```
    {
      "request_id": "0001",
      "applicant_email": "tnobe@amazon.co.jp",
      "approver_email":  "tnobe+1000@amazon.co.jp",
      "type":            "paid",
      "start_date":      "2022/03/25",
      "end_date":        "2022/03/26",
      "desc":            "私用"
    }
    ```
  
  - Demo-Vaction-Request-StateMachine.json
    - 休暇申請を受付てSQSキューにメッセージを送信し、Lambda関数からのタスクトークンを待機するステートマシン
    - 申請の情報や、承認、却下の情報をDynamoDBで管理する
  - このサンプルも、Workflow Studioだけで作成
    - (StateMachineではLambda関数を使っていない。ただし承認結果をCallback用にはLambda関数は使用）

### Workflow Studioだけで作成した(Lambda関数を使わない）画像認識サービス
- workflowStudioフォルダ
  - Demo-Image-Rekognition-StateMachine.json
    - S3バケットに格納された画像をAmazon Rekognitionでラベル検出してDynamoDBに格納するステートマシン
    - S3で発生したイベントは直接EventBridgeに渡され、EventBridgeによりステートマシンが起動






