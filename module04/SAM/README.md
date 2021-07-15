## AWS SAMのデモ
### SAMを使用し、Lamnada関数と統合したAPI GatewayのREST APIを作成する


1. Cloud9のターミナルを開きます。

2. デモ用のフォルダを作成して異動します。

```
mkdir aws-sam-demo
cd  aws-sam-demo
```

3. SAMのバージョンを確認します。

```
sam --version
```

4. SAMのリソースを作成します。デモではPythonのLambda関数を作成します。

```
sam init --runtime python3.7
```

5. テンプレートを選択します。このデモでは、1のAWS Quick Start Templatesを選択します。

```
Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1
```

6. デプロイするパッケージの形式を選択します。このデモでは、1のZipを選択します。

```
What package type would you like to use?
        1 - Zip (artifact is a zip uploaded to S3)
        2 - Image (artifact is an image uploaded to an ECR image repository)
Package type: 1
```

7. プロジェクト名を指定します。このデモではaws-sam-demo-appを入力します。

```
Project name [sam-app]:aws-sam-demo-app
```

8. アプリケーションのテンプレートを指定します。このデモでは1のHello World Exampleを入力します。

```
AWS quick start application templates:
        1 - Hello World Example
        2 - EventBridge Hello World
        3 - EventBridge App from scratch (100+ Event Schemas)
        4 - Step Functions Sample App (Stock Trader)
Template selection: 1
```

10. 下記の内容を確認・編集します。

- SAMテンプレート

  - aws-sam-demo/aws-sam-demo-app/template.yaml 
  - 上記ファイルにHelloWorldFunctionのプロパティに下記を追記して関数名を明示的に指定します。
    -  FunctionName: HelloWorldFunction-SAM

- デプロイするLambda関数

  - aws-sam-demo/aws-sam-demo-app/hello_world/app.py
  - デフォルトで {message: hello world}というJSONを返します。必要に応じて変更します。　

11. SAMでデプロイする前準備をします。

```
cd aws-sam-demo-app
sam build
```

12. デプロイパッケージを格納するためのS3バケットを作成します。(既存のものでもOK)

```
aws s3 mb s3://tnobe-sam-demo
```

13. デプロイパッケージをS3に格納します。

```
sam package --output-template-file packaged.yaml --s3-bucket tnobe-sam-demo
```

14. デプロイを実行します。

```
sam deploy --template-file packaged.yaml --stack-name aws-sam-demo-app --capabilities CAPABILITY_IAM
```








