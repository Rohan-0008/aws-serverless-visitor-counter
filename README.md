# aws-serverless-visitor-counter

# AWS Serverless Visitor Counter

## Overview
A serverless visitor counter built using AWS services.

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
<img width="1910" height="1011" alt="website" src="https://github.com/user-attachments/assets/480d35df-7702-4736-af50-0eefc88afe20" />
<img width="1895" height="906" alt="lambda-function" src="https://github.com/user-attachments/assets/f54d803f-5c2f-4a1a-8457-5511ffd29b15" />
<img width="1917" height="1017" alt="api-gateway" src="https://github.com/user-attachments/assets/5e0118ea-5563-4e38-882f-e3beae889023" />
<img width="1906" height="1011" alt="DynamoDB-table" src="https://github.com/user-attachments/assets/7e11f717-f090-444d-852f-272273e74b20" />
<img width="1917" height="1017" alt="s3-hosting" src="https://github.com/user-attachments/assets/82140bbd-a341-4be4-b111-841cdb08b9bc" />


## Future Improvements
- CloudFront
- Custom Domain
- HTTPS
- Unique Visitor Tracking
