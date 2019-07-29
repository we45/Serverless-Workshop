import jwt
import json


def init(event, context):
    priv = open('private.pem', 'r').read()
    auth_token = jwt.encode({"user": "user", "authenticated": False}, priv, algorithm="RS256")
    return {"statusCode": 200, "body": json.dumps({"token": auth_token.decode()})}


def verify(event, context):
    if 'headers' in event:
        if 'Authorization' in event['headers']:
            pub = open('public.pem', 'r').read()
            try:
                verified = jwt.decode(event['headers']['Authorization'], pub)
                return {"statusCode": 200, "body": json.dumps(verified)}
            except Exception as e:
                print(e)
                return {"statusCode": 403, "body": json.dumps({"error": "Unable to authorize"})}
        else:
            return {"statusCode": 400, "body": json.dumps({"error": "No Authorization code"})}
