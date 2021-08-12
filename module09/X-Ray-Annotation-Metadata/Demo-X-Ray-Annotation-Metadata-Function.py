import json
import time
from aws_xray_sdk.core import xray_recorder


def lambda_handler(event, context):

    orderId= "DEMO-ORDER-0001"
    orderRegion ="Japan"
    
    # Start a subsegment
    subsegment = xray_recorder.begin_subsegment('my_subsegment')

    # Add metadata and annotations
    my_metadata = {"orderRegion":orderRegion}
    subsegment.put_metadata('orderDetail', my_metadata, 'orderProcess')
    subsegment.put_annotation('orderId', orderId)

    #
    time.sleep(5)

    # Close the subsegment and segment
    xray_recorder.end_subsegment()
    #xray_recorder.end_segment()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello, X-Ray Annotation and Metadata Demo')
    }
