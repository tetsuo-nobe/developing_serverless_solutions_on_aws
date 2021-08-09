'''
  グローバル変数の再利用
'''
from datetime import datetime

outside_handler = datetime.now()

def lambda_handler(event, context):

    inside_handler = datetime.now()

    print('outside_handler :' + str(outside_handler))
    print('inside_handler  :' + str(inside_handler))