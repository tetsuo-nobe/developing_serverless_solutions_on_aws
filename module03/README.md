## Amazon Cognito
### AWS CLIを使用したCognitoユーザープールへのサインインの例

1. 必要な情報を環境変数に設定

```
USER_POOL_ID=(CongnitoユーザープールのID)
CLIENT_ID=(CongnitoユーザープールのApplication Client ID)
USER_EMAIL=(ユーザーのメールアドレス)
PASSWORD=(ユーザーのパスワード)
```

2. AWS CLIコマンドでサインイン

```
 aws cognito-idp admin-initiate-auth \
  --user-pool-id ${USER_POOL_ID} \
  --client-id ${CLIENT_ID} \
  --auth-flow ADMIN_NO_SRP_AUTH \
  --auth-parameters "USERNAME=${USER_EMAIL},PASSWORD=${PASSWORD}"
```

3. API GatewayでJWTまたはCognitoオーサライザーが設定されたAPIにアクセスする場合、返されたJWTトークンからIDトークンの値を Authorizationヘッダに設定してリクエストを発行する

```
curl (API Gateway URL) -H "Authorization:(IDトークン)"
```


### AWS CLIを使用してCognitoIDプールから一時的な認証情報を取得する例

1. Cognitoユーザープールでサインインを行いJWTトークンを取得する。JWTトークンの中のIDトークンを環境変数に設定する

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

3. CognitoIDプールからIdentity IDを取得して環境変数に設定

```
IDENTITY_ID=$(aws cognito-identity get-id \
  --identity-pool-id ${IDENTITY_POOL_ID} \
  --logins "${COGNITO_USER_POOL}=${ID_TOKEN}" \
  --query "IdentityId" \
  --output text) && echo ${IDENTITY_ID}
```

4. Identity IDを使って一時的な認証情報を取得

```
aws cognito-identity get-credentials-for-identity \
  --identity-id ${IDENTITY_ID} \
  --logins "${COGNITO_USER_POOL}=${ID_TOKEN}"
```

5. 一時的な認証情報から関連するIAMロール名を表示する

```
export AWS_ACCESS_KEY_ID=(一時的な認証情報の中のアクセスキーID)
export AWS_SECRET_ACCESS_KEY=(一時的な認証情報の中のシークレットアクセスキー)
export AWS_SESSION_TOKEN=(一時的な認証情報の中のセッショントークン)

aws sts get-caller-identity 
```
6. API GatewayのAPIでIAM認証を設定している場合、一時的な認証情報の値からSigV4による署名キーを算出して、Authorizationヘッダに設定してリクエストを発行する

https://docs.aws.amazon.com/ja_jp/general/latest/gr/signature-v4-examples.html




