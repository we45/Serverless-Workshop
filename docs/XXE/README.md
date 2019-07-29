# XXE - Event Injection 

* In your image, navigate over to `/root/labs/Serverless-Workshop/XXE`
* Run `sls plugin install -n serverless-python-requirements`
* Wait for instructor to explain the contents of the lab
 
* Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/XXE/serverless.yml)
* Deploy the function with the command `sls deploy`
* Wait for the function to deploy completely

Now, run: 

```bash
aws s3 cp Pass.docx s3://<name of your s3 bucket/Pass.docx
```

Wait for a few seconds post upload and run:
```bash
sls logs --function xxe
```

You should see the `/etc/passwd` file of the Lambda VM being dumped on screen

### Teardown

* In your image, navigate over to `/root/labs/Serverless-Workshop/XXE`
* Run `sls remove` to remove stack