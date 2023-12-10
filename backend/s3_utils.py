import boto3
from botocore.exceptions import NoCredentialsError
from flask import current_app
import configparser

def upload_file_to_s3(file, filename):
    try:
        s3 = boto3.client('s3', region_name=current_app.config['AWS_REGION_NAME'],
                          aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
                          aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'])

        s3.upload_fileobj(file, current_app.config['S3_BUCKET'], filename)

        # Get the URL of the uploaded file
        file_url = f"https://{current_app.config['S3_BUCKET']}.s3.amazonaws.com/{filename}"

        return file_url
    except NoCredentialsError as e:
        print('Credentials not available')
        raise e
