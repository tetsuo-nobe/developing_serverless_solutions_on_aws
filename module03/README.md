## Amazon Cognito
### AWS CLI を使用したCognito ユーザープールへのサインインの例

0. Cognito ユーザープールを作成し、ユーザー１名のサインアップが完了している前提

1. 必要な情報を環境変数に設定

```
USER_POOL_ID=(CongnitoユーザープールのID)
CLIENT_ID=(CongnitoユーザープールのApplication Client ID)
USER_EMAIL=(ユーザーのメールアドレス)
PASSWORD=(ユーザーのパスワード)
```

2. AWS CLI コマンドでサインイン
    - このコマンドで認証が成功すれば、JWT トークンが返される

```
 aws cognito-idp admin-initiate-auth \
  --user-pool-id ${USER_POOL_ID} \
  --client-id ${CLIENT_ID} \
  --auth-flow ADMIN_NO_SRP_AUTH \
  --auth-parameters "USERNAME=${USER_EMAIL},PASSWORD=${PASSWORD}"
```

3. API Gateway で JW Tまたは Cognito オーサライザーが設定された API にアクセスする場合、返された JWT トークンから ID トークンの値を Authorization ヘッダに設定してリクエストを発行する

```
curl (API Gateway URL) -H "Authorization:(IDトークン)"
```

---

### AWS CLI を使用してCognito ID プールから一時的な認証情報を取得する例

0. Cognito ID プールを作成し、下記を構成済の前提
    - Cognito ユーザープールをアイデンティティプロバイダとして設定している
    - アイデンティティプロバイダで認証された ID には 特定の IAM ロールを付与するように設定している
  
2. Cognito ユーザープールでサインインを行い JWT トークンを取得する
   - JWT トークンの中の ID トークンを環境変数に設定する

```
ID_TOKEN=(JWTトークンの中のIDトークン)
```

2. 必要な情報を環境変数に設定

```
REGION=(リージョンID)
USER_POOL_ID=(CongnitoユーザープールのID)
COGNITO_USER_POOL=cognito-idp.${REGION}.amazonaws.com/${USER_POOL_ID}
IDENTITY_POOL_ID=(Congnito IDプールのID)
```

3. Cognito ID プールから Identity ID を取得して環境変数に設定

```
IDENTITY_ID=$(aws cognito-identity get-id \
  --identity-pool-id ${IDENTITY_POOL_ID} \
  --logins "${COGNITO_USER_POOL}=${ID_TOKEN}" \
  --query "IdentityId" \
  --output text) && echo ${IDENTITY_ID}
```

4. Identity ID を使って IAM ロールの一時的な認証情報を取得

```
aws cognito-identity get-credentials-for-identity \
  --identity-id ${IDENTITY_ID} \
  --logins "${COGNITO_USER_POOL}=${ID_TOKEN}"
```

5. 一時的な認証情報から関連する IAM ロール名を表示する

```
export AWS_ACCESS_KEY_ID=(一時的な認証情報の中のアクセスキーID)
export AWS_SECRET_ACCESS_KEY=(一時的な認証情報の中のシークレットアクセスキー)
export AWS_SESSION_TOKEN=(一時的な認証情報の中のセッショントークン)

aws sts get-caller-identity 
```
6. API Gateway の API で IAM 認証を設定している場合、一時的な認証情報の値から SIGv4 による署名キーを算出して、Authorization ヘッダに設定してリクエストを発行する
https://docs.aws.amazon.com/ja_jp/general/latest/gr/signature-v4-examples.html

- 下記は、[awscurl](https://github.com/okigan/awscurl) というツールを使用している例
```
awscurl  https://xxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/dev/iam  \
    --region ap-northeast-1 \
    --service execute-api
```



