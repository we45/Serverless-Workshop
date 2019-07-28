# Basics - Serverless Events

This lesson is a basic lesson in triggering serverless functions for API Gateway Events. 

* Step 1: In your image, navigate over to `/root/labs/Serverless-Workshop/Basic-API`

```commandline
cd /root/labs/Serverless-Workshop/Basic-API
```

* Step 2: Run `sls plugin install -n serverless-python-requirements`

```commandline
sls plugin install -n serverless-python-requirements
```

* Wait for instructor to explain the contents of the lab

* Step 3: Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/Basic-API/serverless.yml)

* Step 4: Deploy the function with the command `sls deploy`

```commandline
sls deploy
```

* Wait for the function to deploy completely

* Step 5: Now, invoke the function with: 
```commandline

http GET https://XXXXXXXX.execute-api.us-west-2.amazonaws.com/dev/hello

```

### Teardown

* Step 6: In your image, navigate over to `/root/labs/Serverless-Workshop/Basic-API`

```commandline
cd /root/labs/Serverless-Workshop/Basic-API
```

* Step 7: Run `sls remove` to remove stack

```commandline
sls remove
```
