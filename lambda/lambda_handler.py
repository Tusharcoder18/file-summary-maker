import json
import boto3

# Initialize our AWS clients
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # 1. Extract the bucket name and file name from the S3 trigger event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # 2. Define your SNS Topic ARN 
    # IMPORTANT: Replace the string below with your actual SNS Topic ARN from Milestone 2!
    sns_topic_arn = 'arn:aws:sns:ap-south-1:667383781604:file-summary-alerts'
    
    try:
        # 3. Download the file from S3
        response = s3_client.get_object(Bucket=bucket, Key=key)
        # Read the file and split it into a list of rows
        data = response['Body'].read().decode('utf-8').splitlines()
        
        # 4. Count the rows
        row_count = len(data)
        
        # 5. Format the email message
        message = f"Hello!\n\nA new file named '{key}' was successfully uploaded to '{bucket}'.\nTotal rows in this file: {row_count}\n\n- Your AWS Serverless Pipeline"
        
        # 6. Publish the message to your SNS Topic
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject="AWS Pipeline: New File Summary",
            Message=message
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Summary sent successfully!')
        }
        
    except Exception as e:
        print(f"Error processing file: {e}")
        raise e