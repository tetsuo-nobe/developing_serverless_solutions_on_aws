'''
  /tmp領域の再利用
'''
import json
import os
import datetime

# ファイルパス
filepath = "/tmp/demo.txt"

# ファイルが存在していなければ作成する
if  not os.path.exists(filepath):
    print("*** ファイルを作成します。 ***")
    now = datetime.datetime.now()
    with open(filepath, "a") as fdata:
        print("Hello Lambda from file:" + str(now), file=fdata)
        
def lambda_handler(event, context):
    # ファイルの内容を読み込み表示する
    with open(filepath, "r") as fdata:
        print("--- ファイルの中身を表示します。 ---")
        for each_line in fdata:
            print(each_line)
    #
    return {
        'statusCode': 200,
        'body': json.dumps('--- Completed ---')
    }
