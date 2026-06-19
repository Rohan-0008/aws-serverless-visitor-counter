# AWS Serverless Visitor Counter

## Overview
A serverless visitor counter built using AWS services.

## Project Description
This project implements a serverless visitor counter using AWS services. The frontend is hosted on Amazon S3, while API Gateway and AWS Lambda handle visitor count requests. Visitor data is stored and updated in Amazon DynamoDB, enabling real-time tracking without managing servers.

## Architecture
<img width="1632" height="4576" alt="VisitorCounterArchitecture" src="https://github.com/user-attachments/assets/17cde38d-077f-40a9-8a99-568c92b96c22" />


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


## Screenshots
## Website Output
<img width="1910" height="1011" alt="website" src="https://github.com/user-attachments/assets/0d34e92c-9b87-4c63-8344-f35a6bd443a6" />

## AWS Lambda Function
<img width="1895" height="906" alt="lambda-function" src="https://github.com/user-attachments/assets/fa7b6951-ab58-440a-b500-8469523fbe25" />

## DynamoDB Table
<img width="1906" height="1011" alt="dynamoDB-table" src="https://github.com/user-attachments/assets/dd27893d-9ede-4d63-9f3e-0c4f1f59be8c" />

## API Gateway Configuration
<img width="1917" height="1017" alt="api-gateway" src="https://github.com/user-attachments/assets/b789b632-6f85-441c-8794-c6e3d0c219c0" />

## S3 Static Website Hosting
<img width="1917" height="1017" alt="s3-hosting" src="https://github.com/user-attachments/assets/650923fb-e4eb-42f4-8b40-6bb750f94845" />


## Future Improvements
- CloudFront
- Custom Domain
- HTTPS
- Unique Visitor Tracking
