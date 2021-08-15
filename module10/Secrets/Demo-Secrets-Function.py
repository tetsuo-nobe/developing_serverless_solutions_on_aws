import boto3
import json
import os
from botocore.exceptions import ClientError

# 初期設定
ssm = boto3.client( 'ssm' )
env_key_user = 'ENV_USER'
env_key_password = 'ENV_PASSWORD'
env_user =  os.getenv(env_key_user)
env_password = os.getenv(env_key_password)
ssm_user_param = os.getenv('SSM_USER')
ssm_password_param = os.getenv('SSM_PASSWORD')
sm_secret_name = os.getenv('SM_SECRETS')
region_name = os.getenv('REGION_NAME')
prefix = "/aws/reference/secretsmanager" 

#　環境変数の内容の表示
def printEnv():
  print("-- ENV -- :" + env_key_user + ":" + env_user)
  print("-- ENV -- :" + env_key_password + ":" + env_password)

#　SSM Parameter Storeの内容の表示
def printSSMParameter():
  # パラメータ名から復号化したパラメータ値を取得
  ssm_response = ssm.get_parameters(
    Names = [
      ssm_user_param,
      ssm_password_param
    ],
    WithDecryption = True
  )
  # パラメータ値を格納する配列を準備
  params = {}
  # 復号化したパラメータ値を配列に格納
  for param in ssm_response[ 'Parameters' ]:
     print("-- SSM Parameter -- :"+param['Name'] + ":" + param['Value'])

#　SecretsS Managerのシークレットの内容の表示
def printSMSecret():

    #  Secrets Manager clientの作成
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=sm_secret_name
        )
    except ClientError as e:
        raise e
    else:
        secret = get_secret_value_response['SecretString']
        secret_dict = json.loads(secret)
        for key in secret_dict.keys():
            print("-- Secret Manager Secret -- :"+ key + ":" + secret_dict[key])
       
#　SSM Parameter StoreのAPIでSecrets Managerのシークレットの取得と表示
def printSMSecretFromSSM():
  # パラメータ名から復号化したパラメータ値を取得
  param_name = prefix + "/" + sm_secret_name
  ssm_response = ssm.get_parameters(
    Names = [
      param_name,
    ],
    WithDecryption = True
  )
  secrets = ssm_response[ 'Parameters' ][0]['Value']
  secret_dict = json.loads(secrets)
  for key in secret_dict.keys():
      print("-- Secret Manager Secret from SSM -- :"+ key + ":" + secret_dict[key])



# メイン関数
def lambda_handler( event, context ):
  try:
    printEnv()
    printSSMParameter()
    printSMSecret()
    printSMSecretFromSSM()
  except Exception as ex:
    print('!!!! Exception !!!!')
    print(ex)
  # 終了
  return {
    'statusCode': 200,
    'body': json.dumps('-- END --')
  }