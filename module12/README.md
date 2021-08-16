
## モジュール12のデモ/サンプル


### CodePipelineを使用したLambda関数のBlue/Greenデプロイ
- このフォルダにあるファイル群が、CodeCommitに格納されている
  - このCodeCommitリポジトリに更新があれば、自動的にCodePipelineが起動し、ソースを取出して下記を実行する
    - CodeBuildのプロジェクトで、buildspace.yamlの内容を実行しsam packageを実行する
      - 出力されたoutputtemplace.yamlは、Buildのアーティファクトとして管理される
    - CodeDeployで outputtemplace.yamlを使用してスタックを作成する
      - SAMテンプレートに記述したLamnda関数のデプロイ構成に基づき、CodeDeployによりBlue/Greenデプロイメントが実施される








