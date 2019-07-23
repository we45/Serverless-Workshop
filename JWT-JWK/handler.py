from jwcrypto import jwk, jwt
import json
import requests
import jwt as jpy
import boto3
from os import environ
from urllib.parse import urlparse

ssm = boto3.client("ssm")
s3 = boto3.client("s3")
bucket = environ.get('BUCKET_NAME')
s3_url = ""


def get_ssm_parameter(key, secure=False):
    value = ssm.get_parameter(Name=key, WithDecryption=secure)
    if 'Parameter' in value:
        if 'Value' in value["Parameter"]:
            return value['Parameter']['Value']
    else:
        raise Exception("Unable to get param")


def main(event, context):
    if 'headers' in event:
        if 'Authorization' in event['headers']:
            try:
                token_headers = jpy.get_unverified_header(
                    event['headers']['Authorization'])
                if 'jku' in token_headers:
                    r = requests.get(token_headers['jku']).json()
                    j = json.dumps(r)
                    keyset = jwk.JWKSet.from_json(j)
                    print("Keyset", keyset)
                    mykey = keyset.get_key(kid="we45")
                    print("Key", mykey)
                    decoded_token = jwt.JWT(
                        key=mykey, jwt=event['headers']['Authorization'])
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


def login(event, context):
    try:
        data = json.loads(event['body'])
        if data['user'] == "admin" and data['password'] == "admin":
            import_key = get_ssm_parameter("jwk-priv-key", secure=True)
            jku_url = get_ssm_parameter("jku-url")
            priv = jwk.JWK.from_json(import_key)
            token = jwt.JWT(header={"alg": "RS256", "jku": jku_url},
                            claims={"user": "user"}
                            )
            token.make_signed_token(priv)
            final = token.serialize()
            return {"statusCode": 200, "body": json.dumps({"user": "user", "token": final})}


    except Exception as e:
        print(e)


def init(event, context):
    key = jwk.JWK.generate(kty="RSA", size=2048)
    json_key = key.export(private_key=True)
    pub_key = json.loads(key.export_public())
    print(pub_key)
    put_ssm = ssm.put_parameter(
        Name="jwk-priv-key",
        Description="Private key for JWK for Serverless Workshop",
        Value=json_key,
        Type="SecureString",
        Overwrite=True
    )
    if 'Version' in put_ssm:
        pub_key['use'] = "sig"
        pub_key['kid'] = "we45"
        pub_key['alg'] = "RS256"
        try:
            final_pub = json.dumps({"keys": [pub_key]}).encode()
            s3.put_object(Body=final_pub, Bucket=bucket, Key="jwks.json", ACL="public-read")
            global s3_url
            s3_url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': bucket,
                    'Key': "jwks.json"
                }
            )
            parsed_parts = urlparse(s3_url)
            fii_in_url = "{}://{}{}".format(parsed_parts.scheme, parsed_parts.netloc, parsed_parts.path)
            jku_url = ssm.put_parameter(
                Name="jku-url",
                Description="JKU URL",
                Value=fii_in_url,
                Type="String",
                Overwrite=True
            )
            return {"statusCode": 200,
                    "body": json.dumps({"url": fii_in_url})}
        except Exception as e:
            print(e)
            return {"statusCode": 400, "body": json.dumps({"error": e.__str__})}
    else:
        return {"statusCode": 200, "body": json.dumps({"error": "Unable to store Private Key"})}
