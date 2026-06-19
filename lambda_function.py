import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):

    response = table.update_item(
        Key={
            'id': 'visits'
        },
        UpdateExpression='SET #c = #c + :inc',
        ExpressionAttributeNames={
            '#c': 'count'
        },
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues='UPDATED_NEW'
    )

    count = int(str(response['Attributes']['count']))

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'visitor_count': count
        })
    }