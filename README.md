# AWS Serverless Visitor Counter

## Project Description
This project implements a serverless visitor counter using AWS services. The frontend is hosted on Amazon S3, while API Gateway and AWS Lambda handle visitor count requests. Visitor data is stored and updated in Amazon DynamoDB, enabling real-time tracking without managing servers.

## Project Architecture Diagram
<img width="1632" height="4576" alt="VisitorCounterArchitecture" src="https://github.com/user-attachments/assets/17cde38d-077f-40a9-8a99-568c92b96c22" />


## Services Used
- Amazon S3
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- AWS IAM

## Features
- Static website hosting using Amazon S3
- Serverless backend with AWS Lambda
- REST API using API Gateway
- Visitor count storage in DynamoDB
- Real-time visitor tracking

## Workflow
1. User opens website hosted on S3.
2. JavaScript calls API Gateway.
3. API Gateway invokes Lambda.
4. Lambda updates and retrieves visitor count from DynamoDB.
5. Count is returned and displayed on the webpage.


## Skills Demonstrated
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- AWS IAM
- Serverless Architecture
- Cloud Deployment
- Event-Driven Computing


## Future Improvements
- CloudFront
- Custom Domain
- HTTPS
- Unique Visitor Tracking
