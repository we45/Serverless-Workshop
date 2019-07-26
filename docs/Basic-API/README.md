# Basics - Serverless Events

This lesson is a basic lesson in triggering serverless functions for API Gateway Events. 

* In your image, navigate over to `/root/labs/Serverless-Workshop/Basic-API`
* Run `sls plugin install -n serverless-python-requirements`
* Wait for instructor to explain the contents of the lab
* Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/Basic-API/serverless.yml)
* Deploy the function with the command `sls deploy`
* Wait for the function to deploy completely

* Now, invoke the function with: 

    ```bash
    http GET https://XXXXXXXX.execute-api.us-west-2.amazonaws.com/dev/hello
    ```

### Teardown

* In your image, navigate over to `/root/labs/Serverless-Workshop/Basic-API`
* Run `sls remove` to remove stack