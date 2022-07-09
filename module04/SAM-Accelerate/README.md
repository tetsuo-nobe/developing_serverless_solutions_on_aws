## AWS SAM Accelerateのデモ
### AWS SAM Accelerateを使用し、Lambda関数と統合したAPI GatewayのREST APIを作成、更新する

1. Cloud9 のターミナルを開きます。

2. SAM CLI のバージョンを確認します。

```
sam --version
```

**1.34.1以上**のバージョンでなければ、アップグレードします。

```
wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
```

```
sudo ./sam-installation/install --update
```

3. サンプル AWS SAM アプリケーションをダウンロードします。

Cloud 9 の Python 環境を考慮し、Pythonのバージョンを敢えて3.7 にしています。

```
sam init --app-template hello-world --name sam-tutorial --package-type Zip --runtime python3.7
```

4. sam-tutorial ディレクトリに移動します。

```
cd sam-tutorial 
```

5. サーバーレスアプリケーションをデプロイし、変更を監視するプロセスを開始します。

実行を確認するプロンプトが表示されたら、Y で応答します。

```
sam sync --watch --stack-name sam-app
```

sync --watch コマンドを初めて実行すると、AWS SAM は AWS CloudFormation デプロイを開始します。

デプロイ後、AWS SAM はサーバーレスアプリケーションへの変更を監視します。

6. Outputsで表示された API Gatewayのエンドポイント URL をメモしておきます。

例
```
Key                 HelloWorldApi                                                                       
Description         API Gateway endpoint URL for Prod stage for Hello World function                    
Value               https://qc0mchii77.execute-api.ap-northeast-1.amazonaws.com/Prod/hello/             
```

7. アプリケーションのコードを変更します。

次の例では、app.py に print関数で `Invoking the updated function` というメッセージを出力しています。

```
import json
def lambda_handler(event, context):
    print("Invoking the updated function")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
```

SAM Accelerate により変更が自動的に適用されます。

8. アプリケーションの変更を確認します。

Cloud 9 で新しいターミナルを開き、curl コマンドで API を Call します。

```
curl  <API GatewayのエンドポイントURL>
```

```
sam logs --stack-name sam-app --tail
```

ログで `Invoking the updated function` が出力されていることを確認します。

確認できたら、Ctrl + c を押下します。

9. クリーンアップ

`sam sync --watch --stack-name sam-app` を実行したターミナルで、Ctrl + c を押下します。

その後、次のコマンドを実行して SAM ｒのリソースを削除します。

```
sam delete --stack-name sam-app
```

確認のプロンプトが表示されたら、すべて Y で応答します。

