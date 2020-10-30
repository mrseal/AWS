# Lambda

## Run AWS Lambda
$ aws lambda invoke --function-name <FunctionName> --payload '{"<jsonKey>": "<jsonValue>"}' out
$ cat out


# CloudWatch
https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/index.html

## Set CloudWatch Alarm State
$ aws cloudwatch set-alarm-state --alarm-name <Alarm_Name> --state-value Alarm --state-reason test
