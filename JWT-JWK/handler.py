from jwcrypto import jwk, jwt
import json
import requests
import jwt as jpy


def main(event, context):
    if 'headers' in event:
        if 'Authorization' in event['headers']:
            try:
                token_headers = jpy.get_unverified_header(event['headers']['Authorization'])
                if 'jku' in token_headers:
                    r = requests.get(token_headers['jku']).json()
                    j = json.dumps(r)
                    keyset = jwk.JWKSet.from_json(j)
                    print("Keyset", keyset)
                    mykey = keyset.get_key(kid="we45")
                    print("Key", mykey)
                    decoded_token = jwt.JWT(key=mykey, jwt=event['headers']['Authorization'])
                    print("Decoded", decoded_token)
                    json_decode = json.loads(decoded_token.claims)
                    print(json_decode)
                    if 'user' in json_decode:
                        if json_decode['user'] == "user":
                            return {"statusCode": 200, "body": json.dumps({"success": "you are a user"})}
                        elif json_decode['user'] == "admin":
                            return {"statusCode": 200, "body": json.dumps({"success": "you are an admin"})}
                        else:
                            return {"statusCode": 400, "body": json.dumps(
                                {"error": "Sorry! Can't figure out what kind of user you are"})}
            except Exception as e:
                print(e)
                return {"statusCode": 400, "body": json.dumps({"error": "Unable to validate JWT"})}