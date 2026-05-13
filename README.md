# File Summary Maker

An event-driven AWS serverless pipeline project that automatically processes uploaded content and triggers email summary workflows using AWS cloud services.

## 🚀 Project Overview

**File Summary Maker** is a serverless AWS project built using an event-driven architecture. The pipeline leverages AWS managed services to automatically react to file uploads and trigger processing workflows without managing any servers.

This project demonstrates practical usage of AWS Serverless technologies including S3, Lambda, SNS, IAM roles/policies, topics and event notifications.

---

## 🛠️ AWS Services Used

- **Amazon S3**
  - Stores uploaded files
  - Configured event notifications on PUT to trigger downstream processing

- **AWS Lambda**
  - Python-based serverless function handler
  - Processes S3 incoming events and executes business logic

- **Amazon SNS**
  - Publishes notifications/messages after processing
  - Enables decoupled event-driven communication

- **AWS IAM**
  - Configured IAM roles and policies
  - Implemented secure permissions between services

---

## 🏗️ Architecture

```text
User Upload (S3)
        │
        ▼
S3 Event Notification
        │
        ▼
Lambda Function (Python)
        │
        ▼
SNS Topic Notification
        │
        ▼
Email Summary to Subscribers

        └──► CloudWatch Logs
```

---

## 📂 Tech Stack

- **Cloud Provider:** AWS
- **Language:** Python
- **Architecture:** Event-Driven Serverless
- **Services:** S3, Lambda, SNS, IAM

---

## 🔐 Security & Permissions

- Configured custom IAM role for Lambda function
- Applied least-privilege access principles
- Secured communication between AWS services

---

## 📘 Learning Outcomes

Through this project, I gained hands-on experience with:

- AWS Serverless Architecture
- Event-driven workflows
- IAM role and policy management
- S3 event notifications
- Lambda function deployment and execution
- SNS-based messaging systems
- Python-based automation

---

## 👨‍💻 Author

Built as a personal AWS cloud project to practice serverless and event-driven architecture concepts.