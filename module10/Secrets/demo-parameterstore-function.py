import boto3
import json
import os
from botocore.exceptions import ClientError

ssm = boto3.client('ssm')
param_name = "Demo-Parameter"

#　SSM Parameter StoreのAPIでSecrets Managerのシークレットの取得と表示
def printSSMParameter():
  # パラメータ名から復号化したパラメータ値を取得
  print('Called')
  ssm_response = ssm.get_parameters(
    Names = [
      param_name
    ],
    WithDecryption = True
  )
  # パラメータ値を格納する配列を準備
  params = {}
  # 復号化したパラメータ値を配列に格納
  for param in ssm_response[ 'Parameters' ]:
     print("-- Parameter Store -- :"+param['Name'] + ":" + param['Value'])

# メイン関数
def lambda_handler( event, context ):
  try:
    printSSMParameter()
  except Exception as ex:
    print('!!!! Exception !!!!')
    print(ex)
  # 終了
  return {
    'statusCode': 200,
    'body': json.dumps('-- END --')
  }