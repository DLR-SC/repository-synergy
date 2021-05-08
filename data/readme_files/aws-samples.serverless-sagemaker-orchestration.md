# Serverless SageMaker Training and Deployment Orchestration

**Important Note: Step Functions now directly integrates with SageMaker [as detailed here](https://docs.aws.amazon.com/step-functions/latest/dg/connectors-sagemaker.html) rather than requiring the management around these actions through Lambda task states.**

[Linear regression](https://en.wikipedia.org/wiki/Linear_regression) is an approach used in machine learning to model a target variable **y** as a linear combination of a vector of explanatory variables **x** and a vector of learned weights **w**. The [Amazon SageMaker](https://aws.amazon.com/sagemaker/) machine learning platform provides a number of [built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) to help customers get up and running training and deploying machine learning models quickly, including [Linear Learner](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) which can be used for training linear regression models.

For a model to predict accurately the data that it is making predictions on must have a similar distribution as the data on which the model was trained. For example, housing prices in many areas of the country are extremely volatile right now, so the distribution of housing price data for one day may be extremely different than a day a week or a month later. In scenarios like this it may be beneficial to frequently retrain and redeploy the model on only the data from the most recent week or month so the model is not biased by the older data that is no longer representative of the ground truth. As [continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery) is to software, this can be thought of as continuous training and deployment for machine learning models.

This example demonstrates how to build a [serverless](https://aws.amazon.com/serverless/#getstarted) pipeline to orchestrate the continuous training and deployment of a linear regression model for predicting housing prices using Amazon SageMaker, [AWS Step Functions](https://aws.amazon.com/step-functions/), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html). Training data is pulled from the [Boston Housing dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/).

The pipeline is setup to optionally be configured to post notifications to [Slack](https://slack.com/), but could also be modified to work with other popular chat apps such as [Facebook Messenger](https://www.messenger.com/).

This repository contains sample code for the Step Functions state machine and the Lambda functions that compose it's steps, as well as an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template for creating the functions and related resources.

To see other powerful examples of Amazon SageMaker in action check out the [Amazon SageMaker Examples repository](https://github.com/awslabs/amazon-sagemaker-examples).

![slack notifications](images/SlackNotifications.png)

## Walkthrough of Architecture
1. CloudWatch Events Schedule Expressions Rule configured to trigger daily executes Step Functions state machine.
1. State machine checks to ensure new training data has been added to S3 since last model training and deployment, collects training data files in configured time interval to be used for current training job, adds them to a training manifest, then creates training job for model.
1. State machine waits for training job to successfully complete by periodically checking the status of the training job.
1. State machine starts deployment of latest trained model to model endpoint in zero-downtime fashion so that there is no disruption for downstream consumers of previously trained model.
1. State machine waits for model deployment to successfully complete by periodically checking the status of the deployment to the endpoint.
1. (Optional) State machine posts notifications to Slack detailing status updates for training and deployment at each step.


![state machine](images/StateMachine.png)

## Walkthrough of State Machine Steps
The orchestration pipeline has a number of state machine steps. A brief explaination of each step can be found below.
- **CheckData (Task)** - Checks the configured S3 bucket for new training data by comparing the date of the last uploaded data file to the date of the most recent data file a successful model training and deployment has been performed on, which is pulled from a [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html) parameter. If new training data is found then the data files in the training interval are added to a training manifest that is uploaded to S3 and the state machine moves into the **StartTrainingJob** step. If no new data is found then the state machine moves into the **NoNewData** step and ends.
- **StartTrainingJob (Task)** - Creates training job for Linear Learner algorithm using training data specified in training manifest uploaded in **CheckData** step. The state machine then moves into **NotifySlack** step to post notification that a training job has started.
- **NotifySlack (Task)** - If Slack notifications are enabled then this step posts the value corresponding to the 'message' key contained in the input JSON to the configured Slack channel, otherwise this step is a no-op. The state machine then moves into the **NotifySlackBranch** step.
- **NotifySlackBranch (Choice)** - Looks at stage of the pipeline and status of the training or deployment job via the input JSON to decide which step to move the state machine into. If it identifies from that model training or deployment is in progress then it moves the state machine into the **CheckStatusWait** step. If it identifies that model training or deployment has failed then it moves the state machine into the **JobFailed** or **DeploymentFailed** step respectively. Finally, if it identifies that the model training job or model deployment has completed successfully then it moves the state machine into the **JobCompleted** or **DeploymentCompleted** step respectively.
- **CheckStatusWait (Wait)** - Waits 60 seconds before moving the state machine into the **GetStatus** step. Model training and (to a lesser extent) deployment jobs can take some time to run. This wait throttles the executions of the Lambda function in the **GetStatus** task step to one per minute so that the pipeline is not overly eager in checking on the status of the model training or deployment job.
- **GetStatus (Task)** - Checks the status of the ongoing model training or deployment job then moves the state machine into the **CheckStatusBranch** step. 
- **CheckStatusBranch (Choice)** - Looks at the status of the training or deployment job via the input JSON to decide which step to move the state machine into. If it identifies that the training or deployment job is complete or has failed it moves the state machine out of the wait/get/check status loop and into the **NotifySlack** step. Otherwise it moves the state machine into the **CheckStatusWait** step to continue the loop.
- **JobCompleted (Pass)** - Cosmetic step used to explicitly show the training job has completed and the training stage is over in the state machine diagram. Moves the state machine into the **DeployModel** step.
- **DeployModel (Task)** - Creates endpoint resources for model and deploys trained model to endpoint. If the endpoint already exists it is updated to use the newly trained model in a zero-downtime fashion. If the endpoint doesn't already exists a new one is created for it. Moves state machine into the **NotifySlack** step.
- **DeploymentCompleted (Pass)** - Cosmetic step used to explicitly show the model deployment has completed and the deployment stage is over in the state machine diagram. Moves the state machine into the **UpdatedParameters** step.
- **UpdateParameters (Task)** - Updates Parameter Store parameter referenced in **CheckData** step to date of latest training file that training job was run on then moves state machine to **End** step to successfully terminate state machine execution.
- **JobFailed (Fail)** - Indicates that there was an error in the model training job causing the state machine execution to fail.
- **DeploymentFailed (Fail)** - Indicates that there was an error in the model deployment causing the state machine execution to fail.


## Running the Example
### (Optional) Preparing Slack
If you would like to enable the pipeline to post notifications to Slack first make sure you're logged in to Slack, then follow the instructions below to prepare the Slack app.
1. [Create an app](https://api.slack.com/apps?new_app=1) ([Documentation](https://api.slack.com/slack-apps#creating_apps))
1. Navigate to the `OAuth & Permissions` tab under `Features`
1. Under the `Permissions Scopes` section add the following permission scopes
    * chat:write:bot
1. Click `Save Changes`
1. Click `Install App to Team` then `Authorize` then note the `OAuth Access Token` as it will be required later
1. Also note the name of the channel you would like the notifications for the bot to be posted to (Ex: general, random, etc) as it will be required later as well

### Deploying the Pipeline on AWS
#### Option 1: Launch the CloudFormation Template in US West - Oregon (us-west-2)
The backend infrastructure can be deployed in US West - Oregon (us-west-2) using the provided CloudFormation template.
Click **Launch Stack** to launch the template in the US West - Oregon (us-west-2) region in your account:

[![Launch Stack into Oregon with CloudFormation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=ServerlessSageMakerOrchestration&templateURL=https://s3-us-west-2.amazonaws.com/aws-samples-artifacts-us-west-2/serverless-sagemaker-orchestration/continuous_sagemaker.output.yaml)

(On the last page of the wizard, make sure to:

1. Click the checkboxes to give AWS CloudFormation permission to **"create IAM resources"** and **"create IAM resources with custom names"**
1. Follow the instructions to **"Create Change Set"** 
1. Click **"Execute"**
)

#### Option 2: Launch the CloudFormation Template Manually 
If you would like to deploy the template manually, you need a S3 bucket in the target region, and then package the Lambda functions into that S3 bucket by using the `aws cloudformation package` utility.

Set environment variables for later commands to use (if you do not wish to enable Slack notifications you do not need to set `ATOKEN` or `CHANNEL`):

```bash
S3BUCKET=[REPLACE_WITH_BUCKET_TO_UPLOAD_TEMPLATE_ARTIFACTS_TO]
REGION=[REPLACE_WITH_REGION_YOU_WISH_TO_DEPLOY_TO]
STACKNAME=[REPLACE_WITH_DESIRED_STACK_NAME]
SAGEMAKERROLE=[REPLACE_WITH_SAGEMAKER_EXECUTION_ROLE]
ATOKEN=[REPLACE_WITH_OAUTH_ACCESS_TOKEN]
CHANNEL=[REPLACE_WITH_SLACK_CHANNEL_NAME]
```

Then go to the `cloudformation` folder and use the `aws cloudformation package` utility

```bash
cd cloudformation

aws cloudformation package --region $REGION --s3-bucket $S3BUCKET --template continuous_sagemaker.serverless.yaml --output-template-file continuous_sagemaker.output.yaml
```
Last, deploy the stack with the resulting yaml (`image_moderator.output.yaml`) through the CloudFormation Console or command line:

```bash
aws cloudformation deploy --region $REGION --template-file continuous_sagemaker.output.yaml --stack-name $STACKNAME --capabilities CAPABILITY_NAMED_IAM --parameter-overrides SageMakerExecutionRole=$SAGEMAKERROLE SlackAccessToken=$ATOKEN SlackChannel=$CHANNEL
```

If you would like Slack notifications disabled for your pipeline then from the console ensure `EnableSlack` is set to **False** or use the following command to deploy from the command line instead:

```bash
aws cloudformation deploy --region $REGION --template-file continuous_sagemaker.output.yaml --stack-name $STACKNAME --capabilities CAPABILITY_NAMED_IAM --parameter-overrides SageMakerExecutionRole=$SAGEMAKERROLE EnableSlack="False"
```

### Uploading Training Data
Lastly we need to upload training data for the model to train on. To do this we've provided a Jupyter notebook to run from a SageMaker notebook instance. Follow the instructions below to launch a SageMaker notebook instance and run the notebook.
1. [Launch a SageMaker Notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-setup-working-env.html)
1. Download the [serverless-sagemaker-orchestration.ipynb](../master/notebooks/serverless-sagemaker-orchestration.ipynb) from this repository to your desktop.
1. Wait for your SageMaker Notebook instance to finish launching then open it.
1. From the Jupyter console click 'Upload' in the top right then upload the `serverless-sagemaker-orchestration.ipynb` you downloaded to your desktop. Click 'Upload' again to finalize.
1. Open `serverless-sagemaker-orchestration.ipynb` by clicking it from the Jupyter console.
1. Run the cells under `Generate and Upload Housing Price Data` to upload training data for the model to S3.


## Testing the Example
Once you have deployed the pipeline and uploaded training data to S3 your pipeline is ready to run the next time it is triggered by the CloudWatch Events rule. If you would like to test it manually before then you can use the cells under `Generate JSON For Testing Execution` in the `serverless-sagemaker-orchestration.ipynb` to generate JSON for this purpose. Follow the instructions below to generate this JSON and use it trigger a Step Functions state machine execution:
1. Navigate back to the `serverless-sagemaker-orchestration.ipynb` running on your SageMaker notebook instance and run the cells under `Generate JSON For Testing Execution`. Copy the output to your clipboard.
1. Navigate to the [Step Functions console](https://console.aws.amazon.com/states/home)
1. Select the state machine created for the pipeline by clicking it's name in the `State machines` table.
1. Scroll down to the `Executions` table and click `Start execution`.
1. In the `New execution` modal paste the JSON copied earlier from your clipboard.
1. Click `Start execution` to invoke an execution of the state machine.

After starting the state machine execution you can watch as it steps through the states from the console.

## Performing Inference On the Model Endpoint
Upon the first successful execution of your pipeline your model will be deployed to a SageMaker model endpoint where it queried to perform price inference from home data submitted to it. For an example of this in action navigate back to the `serverless-sagemaker-orchestration.ipynb` running on your SageMaker notebook instance and run the cells under `Leverage Model Endpoint For Inference`.
The first cell shows how to create a predictor object to perform inference queries against your model endpoint. The next cells are example inference queries for both a single house and multiple houses at once.

![notebook output](images/Notebook.png)


## Cleaning Up the Stack Resources

To remove all resources created by this example, do the following:

1. Stop and delete the SageMaker Notebook instance.
1. [Manually delete the S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/delete-bucket.html) (buckets that aren't empty cannot be deleted by CloudFormation)
1. Delete the CloudFormation stack.
1. Delete the CloudWatch log groups associated with each Lambda function created by the CloudFormation stack.


## CloudFormation Template Resources
The following sections explain all of the resources created by the CloudFormation template provided with this example.

### Amazon CloudWatch Events
- **ServerlessSageMakerOrchestrationRule** - Scheduled expression rule configured to invoke Step Function state machine exceution daily.

### AWS Step Functions
- **SageMakerStateMachine** - Step Functions state machine that orchestrates training and deployment pipeline.

### AWS Lambda
- **CheckDataFunction** - Lambda function implementing task of **CheckData** step of state machine
- **StartTrainingJobFunction** - Lambda function implementing task of **StartTrainingJob** step of state machine
- **NotifySlackFunction** - Lambda function implementing task of **NotifySlack** step of state machine
- **GetStatusFunction** - Lambda function implementing task of **GetStatus** step of state machine
- **DeployModelFunction** - Lambda function implementing task of **DeployModel** step of state machine
- **UpdateParametersFunction** - Lambda function implementing task of **UpdateParameters** step of state machine

### AWS IAM
- **CheckDataFunctionRole** - IAM Role with policy that allows Lambda function to read value of **SSMParameter**, get and put objects to **S3Bucket**, and write log messages to CloudWatch Logs.
- **StartTrainingJobFunctionRole** - IAM Role with policy that allows Lambda function to create SageMaker model training jobs, pass a configured IAM role to SageMaker, and write log messages to CloudWatch Logs.
- **NotifySlackFunctionRole** - IAM Role with policy that allows Lambda function to write log messages to CloudWatch Logs.
- **DeployModelFunctionRole** - IAM Role with policy that allows Lambda function to create and update SageMaker model endpoint resources, pass a configured execution role to SageMaker, and write log messages to CloudWatch Logs.
- **UpdateParametersFunctionRole** - IAM Role with policy that allows Lambda function to write value of read value of **SSMParameter** and write log messages to CloudWatch Logs.

### Amazon S3
- **S3Bucket** - S3 bucket to hold model training data and trained model artifacts.

### AWS Systems Manager
- **SSMParameter** - Parameter Store parameter holding the date of the most recent data file a successful model training and deployment has been performed on.


## License Summary

This sample code is made available under a modified MIT license. See the LICENSE file.
