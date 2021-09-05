
## モジュール11のデモ/サンプル


### 同時アクセス数の増加に伴いLambda関数のインスタンスも増加する
- demo-concurrent5.jsonのステートマシンを実行
  - Lambda関数 ConcurrentDemoFunctionのインスタンスは5個になる
- demo-concurrent10.jsonのステートマシンを実行
  - Lambda関数 ConcurrentDemoFunctionのインスタンスは計10個になる

### AWS Lambda × Amazon SQS
- sqsフォルダ
  - Demo-SQS-FunctionA.py
  - Demo-SQS-FunctionB.py
    - これらのLambda関数は、基本的に全て処理内容は同じで、それぞれトリガーで設定されたSQSのQueueへポーリングして取得したメッセージを表示する。
    - ただし、メッセージ内容が "abort" だった場合は強制的にエラーを発生させている。









