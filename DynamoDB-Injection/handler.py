import json
import boto3

db = boto3.client('dynamodb')


def main(event, context):
    if 'body' in event:
        jbody = json.loads(event['body'])
        if 'db' in jbody and 'search_term' in jbody and 'search_operator' in jbody \
                and 'search_field' in jbody:

            response = db.scan(TableName=jbody['db'], Select='ALL_ATTRIBUTES', ScanFilter={
                jbody['search_field']: {"AttributeValueList": [{"S": jbody['search_term']}],
                                        "ComparisonOperator": jbody['search_operator']}
            })
            if 'Items' in response:
                return {"statusCode": 200, "body": json.dumps(response['Items'])}
            else:
                return {"statusCode": 404, "body": json.dumps([])}
        else:
            return {"statusCode": 404, "body": json.dumps({"error": "Mandatory fields not in query"})}
