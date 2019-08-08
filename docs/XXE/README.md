# XXE - Event Injection 

**Note:** If you have not setup your aws cli follow [AWS-CLI-Configuration](aws-configure/README.md) under the `Setup` section*

* Step 1: In your image, navigate over to `/root/labs/Serverless-Workshop/XXE`

```commandline
cd /root/labs/Serverless-Workshop/XXE
```

* Step 2: Run `sls plugin install -n serverless-python-requirements`

```commandline
sls plugin install -n serverless-python-requirements
```

* Wait for instructor to explain the contents of the lab
 
* Step 3: Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/XXE/serverless.yml)

* Step 4: Deploy the function with the command `sls deploy`

```commandline
sls deploy
```

* Wait for the function to deploy completely

* Step 5: Now, run: 

```commandline
aws s3 ls | grep we45-sls-xxe-
```

```commandline
aws s3 cp Pass.docx s3://< name of your s3 bucket >/Pass.docx
```

* Step 6: Wait for a few seconds post upload and run:

```commandline
sls logs --function xxe
```

You should see the `/etc/passwd` file of the Lambda VM being dumped on screen

### Teardown

* Step 7: In your image, navigate over to `/root/labs/Serverless-Workshop/XXE`

```commandline
cd /root/labs/Serverless-Workshop/XXE
```

* Got to aws console and click s3 and then delete `we45-sls-xxe-` bucket

* Step 8: Run `sls remove --force` to remove stack

```commandline
sls remove --force
```
