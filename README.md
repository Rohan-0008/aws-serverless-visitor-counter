# aws-serverless-visitor-counter

# AWS Serverless Visitor Counter

## Overview
A serverless visitor counter built using AWS services.

## Architecture
[Insert architecture-diagram.png]

## Services Used
- Amazon S3
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- AWS IAM

## Workflow
1. User opens website hosted on S3.
2. JavaScript calls API Gateway.
3. API Gateway invokes Lambda.
4. Lambda updates and retrieves visitor count from DynamoDB.
5. Count is returned and displayed on the webpage.

## Architecture Diagram

## Screenshots

## Future Improvements
- CloudFront
- Custom Domain
- HTTPS
- Unique Visitor Tracking
