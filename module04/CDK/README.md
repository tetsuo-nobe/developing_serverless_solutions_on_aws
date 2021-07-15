## AWS CDKのデモ
### CDKを使用し、Lamnada関数と統合したAPI GatewayのREST APIを作成する


1. Cloud9のターミナルを開きます。

2. デモ用のフォルダを作成して異動します。

```
mkdir aws-cdk-demo
cd  aws-cdk-demo
```

3. CDKのバージョンを確認します。

```
cdk --version
```

4. CDKのリソースを作成します。デモではTypeScriptを使用します。

```
cdk init app --language typescript
```

5. CDKのコンストラクタモジュールをインストールします。@以降のバージョンは、手順3で確認したバージョンに合わせます。

```
npm install @aws-cdk/assets@1.111.0
npm install @aws-cdk/aws-s3-assets@1.111.0
npm install @aws-cdk/aws-lambda@1.111.0
npm install @aws-cdk/aws-apigateway@1.111.0
```

6. デプロイするPythonのLambda関数を作成します。このデモでは、srcディレクトリにindex.pyとして作成します。

```
(このフォルダのindex.pyの内容を参照してください。)
```

7. lib/aws-cdk-demo-stack.tsを編集して、Lambda関数とAPI GatewayのAPIをデプロイするコードを追記します。

```
(このフォルダのaws-cdk-demo-stack.tsの内容を参照してください。)
```

8. TypeScriptをJavaScriptに変換します。

```
npm run build
```

9. CDKを使ってスタックを作成します。

```
cdk deploy
```

10. 作成したスタックを削除する場合は下記を実行します。

```
cdk destroy
```




