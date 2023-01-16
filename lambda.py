import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    products = json.loads(event["body"])
    
    preference_data = {
       "items": products["items"]
    }

    payment_response = sdk.payment().create(event)
    
    preference_response = sdk.preference().create(preference_data)
    
    payment = payment_response["response"]
    
    status =payment["status"]

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        
        "body": json.dumps(
            preference_response["response"]
        ),
    }
