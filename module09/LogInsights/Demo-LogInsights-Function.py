import json
import random
from datetime import datetime
from aws_lambda_powertools import Logger
logger = Logger(service="logger_demo")

def usePrint(price,quantity,product,user,now):
    log =    {
        "level": "INFO",
        "message": {
            "PriceInCart": price,
            "QuantityInCart": quantity,
            "ProductId": product,
            "UserId": user 
        },
        "timestamp": now
    }
    print(json.dumps(log))

def useLambdaPowerTool(price,quantity,product,user):
    logger.info(  
        {
            "PriceInCart": price,
            "QuantityInCart": quantity,
            "ProductId": product,
            "UserId": user
        }
     )

def lambda_handler(event, context):
    #
    productid = random.randrange(1,10,1)
    product = "P" + str(productid)
    quantity = random.randrange(1,10,1)
    price = quantity * 100
    userid = random.randrange(1,6,1)
    user = "tnobe" + str(userid)
    now = str(datetime.now())
    #
    #usePrint(price,quantity,product,user,now)
    #
    useLambdaPowerTool(price,quantity,product,user)
    #
    return {
        'statusCode': 200,
        'body': json.dumps('-- END ')
    }
