## AWS SAM のサンプル
### Lamnada関数と統合したAPI GatewayのREST APIを作成する
##### ( SAMテンプレートの中に CloudFormationの記述を埋め込むパターン)

* SAMテンプレート
  - Lambda関数 HelloWorldFunction は、SAMのリソースタイプとして記述
  - Amazon API Gateway の REST API や Lamnda関数との連携設定は、CloudFormation のリソースタイプとして記述