## AWS SAMのデモ
### SAMを使用し、Lambda関数と統合したAPI GatewayのREST APIを作成する


1. Cloud9のターミナルを開きます。

2. デモ用のフォルダを作成して移動します。

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


11. SAMでサーバーレスアプリケーションを構築してテストやデプロイする前準備を行います。

```
cd aws-sam-demo-app
sam build
```

12. SAMを使用しローカルでテストします。

```
sam local invoke 
```

[その他のローカルテスト用のコマンド](#その他のローカルテスト用のコマンド) 
<br />
<br />


この後、デプロイを実施します。
sam deploy --guidedを使わない場合は下の12番のタスクを実行します。 
<br />
[sam deploy --guidedを使う場合はこちら](#デプロイをシンプルにするために) 
 
 
13. デプロイパッケージを格納するためのS3バケットを作成します。(既存のものでもOK)

```
aws s3 mb s3://tnobe-sam-demo
```

14. デプロイパッケージをS3に格納します。

```
sam package --output-template-file packaged.yaml --s3-bucket tnobe-sam-demo
```

15. デプロイを実行します。

```
sam deploy --template-file packaged.yaml --stack-name aws-sam-demo-app --capabilities CAPABILITY_IAM
```

以上でデプロイは完了です！

16. SAMで作成したスタックを削除するには、`sam delete` を実行します。

```
sam delete
```
 <br />
 <br />
 <br />

## デプロイをシンプルにするために 
 
sam deploy --guidedを使うと、sam deployのパラメータをファイルに保存し、以後、容易にデプロイできます。

```
sam deploy --guided
```

以後、対話的に進めていくと、指定した内容がsam deploy実行時に必要パラメータとしてファイル（デフォルト:samconfig.toml）保存され、その後デプロイが実行されます。

```
Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Not found

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app]: aws-sam-demo-app
        AWS Region [ap-northeast-1]: 
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [y/N]: y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: 
        HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
        Save arguments to configuration file [Y/n]: y
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 

        Looking for resources needed for deployment: Found!

                Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-1atvkbrimmtfv
                A different default S3 bucket can be set in samconfig.toml
(以下略)
```

1回目のデプロイが完了後、2回目のsam deployを実施する時は、ファイル（デフォルト:samconfig.toml）が存在する場合は、そこから必要なパラメータが取得されるので、下記のように簡単なコマンドでデプロイできます。

```
sam deploy 
```

 <br />
 <br />
 <br />

## その他のローカルテスト用のコマンド 

Lambda関数
```
sam local start-lambda
```

```
aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt
```

API Gateway
```
sam local start-api
```

```
curl http://127.0.0.1:3000/hello
```




