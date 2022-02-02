## AWS CDKのデモ
### CDKを使用し、Lamnada関数と統合したAPI GatewayのREST APIを作成する

### 注意：現在、Cloud9はデフォルトでCDK v2がインストールされているため、下記手順はCloud9では、そのままでは使用できません。
### CDK v1がインストールされている環境でご使用ください。

1. デモ用のフォルダを作成して異動します。

```
mkdir aws-cdk-demo
cd  aws-cdk-demo
```

2. CDKのバージョンを確認します。

```
cdk --version
```

3. CDKのリソースを作成します。デモではTypeScriptを使用します。

```
cdk init app --language typescript
```

4. CDKのコンストラクタモジュールをインストールします。@以降のバージョンは、手順3で確認したバージョンに合わせます。

```
npm install @aws-cdk/assets@1.111.0
npm install @aws-cdk/aws-s3-assets@1.111.0
npm install @aws-cdk/aws-lambda@1.111.0
npm install @aws-cdk/aws-apigateway@1.111.0
```

5. デプロイするPythonのLambda関数を作成します。このデモでは、srcディレクトリにindex.pyとして作成します。

```
(このフォルダのindex.pyの内容を参照してください。)
```

6. lib/aws-cdk-demo-stack.tsを編集して、Lambda関数とAPI GatewayのAPIをデプロイするコードを追記します。

```
(このフォルダのaws-cdk-demo-stack.tsの内容を参照してください。)
```

7. TypeScriptをJavaScriptに変換します。

```
npm run build
```

8. CDKを使ってスタックを作成します。
(初回の場合は、先にcdk bootstrap を実行して CDKが使用するS3バケットを作成します。)

```
cdk deploy
```

9. 作成したスタックを削除する場合は下記を実行します。

```
cdk destroy
```




