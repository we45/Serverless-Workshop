# Basics - Serverless Events

This lesson is a basic lesson in triggering serverless functions for Non-API Gateway Events. 

In this lesson, we will trigger a Serverless Function whenever messages are published over a particular SNS (Simple Notification Service) Topic (Channel)

* In your image, navigate over to `/root/labs/Serverless-Workshop/Basic-Event`
* Wait for instructor to explain the contents of the lab
* Let's look at the contents of the `serverless.yml` [here](https://github.com/we45/Serverless-Workshop/blob/master/Basic-Event/serverless.yml)
* Deploy the function with the command `sls deploy`
* Wait for the function to deploy completely

* Now access your AWS Console and look for Simple Notification Service or `SNS`

![SNS-Search](img/sns-search.png)

* Click to go to SNS Main Page, which looks like this and click on topics to find the ARNS of all your current topics

![SNS-Topics](img/sns-topics.png)

* Now Copy the Topic-ARN

![Copy-Topics](img/copy-topic-arn.png)

* In your lab environment, in the CLI, enter the following command

*You have to have configured AWS CLI by now*

```bash
aws sns publish --topic-arn "<Copied ARN>" --message "I am going to be pwning Serverless Functions soon!"

```
**Remember to substitute the `<Copied ARN>` with the ARN that you copied from the previous step**

* Now, let's see whether the Serverless Function worked, by running the following command

```bash

sls logs --function sns-reactor
```
```commandline
START RequestId: 44478848-a777-45e0-a1cf-e11cd499071e Version: $LATEST
END RequestId: 44478848-a777-45e0-a1cf-e11cd499071e
REPORT RequestId: 44478848-a777-45e0-a1cf-e11cd499071e	Duration: 1.41 ms	Billed Duration: 100 ms 	Memory Size: 512 MB	Max Memory Used: 52 MB

START RequestId: 1066617f-4b0f-4683-b91b-ffbd81e40a86 Version: $LATEST
{'Records': TRUNCATED

```