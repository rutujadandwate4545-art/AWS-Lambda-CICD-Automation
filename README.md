
# Automating CI/CD Pipelines Using AWS Lambda

## 1. Project Objective
To automate CI/CD pipeline monitoring and related tasks using AWS Lambda and AWS CodePipeline.

## 2. AWS Services Used
- AWS Lambda
- AWS CodePipeline
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch
- Amazon S3 (optional deployment target)

## 3. Project Workflow
1. Store application code in GitHub.
2. AWS CodePipeline retrieves the application code.
3. CodePipeline runs the configured pipeline stages.
4. Amazon EventBridge detects pipeline state changes.
5. AWS Lambda processes the event and logs pipeline details.
6. Amazon CloudWatch stores Lambda execution logs.

## 4. Project Files
- index.html: Sample web application.
- lambda_function.py: Lambda event-processing code.
- README.md: Project documentation.

## 5. Implementation Steps
1. Create a sample HTML application.
2. Create a Python Lambda function.
3. Configure the required IAM permissions.
4. Create an AWS CodePipeline pipeline.
5. Configure an EventBridge rule to invoke Lambda.
6. Test the workflow and inspect CloudWatch logs.

## 6. Security Practices
- Follow the principle of least privilege for IAM permissions.
- Never upload AWS access keys or passwords to GitHub.
- Review AWS resource permissions before deployment.

## 7. Learning Outcomes
- Understanding CI/CD automation.
- Learning AWS Lambda and EventBridge integration.
- Monitoring executions with CloudWatch.
- Understanding IAM permissions and deployment workflows.

## 8. Project Status
Implementation and testing steps will be documented as the project progresses.
