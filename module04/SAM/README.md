## AWS SAMのデモ
### SAM を使用し、Lambda関数と統合したAPI GatewayのREST APIを作成する
* **SAM CLI バージョン 1.90.0 以上がインストール済の前提です**
  - SAM CLI　のインストールについては[こちら](#AWS-SAM-CLI-のインストール)をご参照ください
    
1. Mac や Linux の場合はターミナル、Windows の場合はコマンドプロンプトを開きます。

1. 下記を実行して SAM のバージョンが 1.90.0 以上であることを確認して下さい。

        
        sam --version
        

1. SAM のリソースを作成します。デモでは Python の Lambda 関数を作成します。

        
        sam init --runtime python3.11
        

1. テンプレートを選択します。このデモでは、1のAWS Quick Start Templatesを選択します。

        
        Which template source would you like to use?
                1 - AWS Quick Start Templates
                2 - Custom Template Location
        Choice: 1
        

1. アプリケーションのテンプレートを選択します。このデモでは、1 の Hello World Example を選択します。

        
        Choose an AWS Quick Start application template
                1 - Hello World Example
                2 - Hello World Example With Powertools for AWS Lambda
                3 - Infrastructure event management
                4 - Multi-step workflow
                5 - Lambda EFS example
                6 - Serverless Connector Hello World Example
                7 - Multi-step workflow with Connectors
       Template: 1
        

1. AWS X-Ray によるトレース取得や CloudWatch Application Insights の有効化または無効化を指定します。このデモでは、そのまま Enter キーを押下して N (無効化)を選択します。

        
        Based on your selections, the only Package type available is Zip.
        We will proceed to selecting the Package type as Zip.

        Based on your selections, the only dependency manager available is pip.
        We will proceed copying the template using pip.

        Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: 
        
        Would you like to enable monitoring using CloudWatch Application Insights?
        For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: 
        
        Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]: 
        

1. プロジェクト名を指定します。このデモでは aws-sam-demo-app を入力します。

        
        Project name [sam-app]:aws-sam-demo-app
        


1. 下記の内容を確認・編集します。

        - SAM テンプレート

        - aws-sam-demo/aws-sam-demo-app/template.yaml 
        - 上記ファイルにHelloWorldFunctionのプロパティに下記を追記して関数名を明示的に指定します。
        -  FunctionName: HelloWorldFunction-SAM

        - デプロイするLambda関数

        - aws-sam-demo/aws-sam-demo-app/hello_world/app.py
        - デフォルトで {message: hello world}というJSONを返します。必要に応じて変更します。　


1. SAM でサーバーレスアプリケーションの依存性を解決して、テストやデプロイする前準備を行います。ここでは、`--use-container` オプションを指定してコンテナを使ってビルドしていますので、Lambda 関数のランタイムとローカルのランタイムのバージョンが不一致でも問題ありません。ただし、Docker がインストールされている必要があります。

        
        cd aws-sam-demo-app
        sam build  --use-container
        

1. SAM を使用しローカルでテストします。(Docker が必要です。)

        
        sam local invoke 
        


    - [その他のローカルテスト用のコマンド](#その他のローカルテスト用のコマンド) 
    - この後、デプロイを実施します。
    - sam deploy --guidedを使わない場合は下の下記のタスクを実行します。 
        <br />
    - [sam deploy --guidedを使う場合はこちら](#デプロイをシンプルにするために) 
        
 
1. デプロイパッケージを格納するためのS3バケットを作成します。(既存のものでもOK)

        
        aws s3 mb s3://tnobe-sam-demo
        

1. デプロイパッケージをS3に格納します。

        
        sam package --output-template-file packaged.yaml --s3-bucket tnobe-sam-demo
        

1. デプロイを実行します。

        
        sam deploy --template-file packaged.yaml --stack-name aws-sam-demo-app --capabilities CAPABILITY_IAM
        

    - 以上でデプロイは完了です！

1. SAMで作成したスタックを削除するには、`sam delete` を実行します。
  - (下記では設定しませんが、`--no-prompts` オプションをつけると非対話モードで実行します。）

        
        sam delete
        
 <br />
 <br />
 <br />

## デプロイをシンプルにするために 
 
sam deploy --guidedを使うと、sam deployのパラメータをファイルに保存し、以後、容易にデプロイできます。

        
        sam deploy --guided
        

以後、対話的に進めていくと、指定した内容がsam deploy実行時に必要パラメータとしてファイル（デフォルト:samconfig.toml）保存され、その後デプロイが実行されます。
HelloWorldFunction may not have authorization defined, Is this okay? では `y` を指定します。

        
   Configuring SAM deploy
   ======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [aws-sam-demo-app]: 
        AWS Region [ap-northeast-1]: 
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: 
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: 
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]: 
        HelloWorldFunction has no authentication. Is this okay? [y/N]: y
        Save arguments to configuration file [Y/n]: 
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 

        Looking for resources needed for deployment:


    (以下略)
 

変更セットの確認で `y` を入力します。

    Previewing CloudFormation changeset before deployment
    ======================================================
    Deploy this changeset? [y/N]: y

        (以下略)

        
リモートでのテストを実行します。

      sam remote invoke --stack-name aws-sam-demo-app --region ap-northeast-1


1回目のデプロイが完了後、2回目のsam deployを実施する時は、ファイル（デフォルト:samconfig.toml）が存在する場合は、そこから必要なパラメータが取得されるので、下記のように簡単なコマンドでデプロイできます。

        
        sam deploy 
        

 <br />
 <br />
 <br />

---

## その他のローカルテスト用のコマンド 

Lambda関数
        
        sam local start-lambda
        

        
        aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt
        

API Gateway
        
        sam local start-api
        

        
        curl http://127.0.0.1:3000/hello

---
        
## AWS SAM CLI のインストール

* https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/install-sam-cli.html
* 以下は Linux でのインストール例

        mkdir tmp && cd tmp
        wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
        unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
        sudo ./sam-installation/install --update
        cd ..
        rm -rf tmp



