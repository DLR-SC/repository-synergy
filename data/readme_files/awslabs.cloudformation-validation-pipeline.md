Usage
-----

A demo and deployment guide describing this solution are available on the AWS Answers website.

To start writing your own tests and pipelines to test your templates it's likely your going to want to customize which tests are run and even write your own tests.

To ensure that any binary dependencies you may have are built for the correct platform it is recommended to create a new ec2 instance using the amzn-ami-hvm-2016.03.3.x86_64-gp2 AMI and run the build process from there.

The following s3 permissions are required for the IAM user/role configured in the aws cli:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

Ensure that pip and setuptools are up to date:
```bash
sudo -H pip install --upgrade setuptools pip
```

Clone the validation pipeline repo:
```bash
git clone https://github.com/awslabs/aws-cloudformation-validation-pipeline.git
```

Install:
```bash
cd aws-cloudformation-validation-pipeline
sudo -H python setup.py install
```

Now you're ready to start building tests and pipelines, to get going create a project skeleton:
```bash
cd ~/
cfn-validation-pipeline-skeleton
cd validation_pipeline
```

In the validation_pipeline folder you will find all the required cloudformation templates, lambda function code, html docs and unit tests

Building/deploying dependencies, Lambda function zips and CloudFormation templates to S3 is done using the deployment utility:
```bash
cfn-validation-pipeline-deploy my-cfn-pipeline-bucket
```

***Note:*** this command has several configurable options, to view help for the deployment tools run the command with the --help argument

Now you can launch stacks from the cloudformation console using the s3 location for the desired cloudformation template in the output of the previous command.

Creating your own tests
-----------------------

This can be done by creating a new folder in the 'lambda_functions' folder. The folder should contain:
* python file(s) - this is installed into the lambda function and executed when the pipeline runs.
* requirements.txt [optional] - a list of all python packages that are required. Can include pip modules or custom modules stored in the 'lambda_functions/lib/' folder

Using the CFNPipeline class in your function greatly simplifies writing tests and is recommended. The included tests can be used as examples on usage for both pre-create and post-create tests. The validate_template and ami_check are fairly simple examples of pre and post create tests respectively. HTML API docs for usage of CFNPipeline are available in the 'docs' folder.

Adding tests to the template and pipeline
-----------------------------------------
Custom tests can be added to the 'cloudformation/central-microservices.template' file and added to the pipeline by modifying 'cloudformation/main-pipeline.template' file.

Once you've authored your new tests and pipeline it can be deployed to s3 using the cfn-validation-pipeline-deploy command.
