import boto3
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import yaml

class S3Uploader:
    def __init__(self, aws_access_key, aws_secret_key, region_name, bucket_name):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name
        )
        self.bucket_name = bucket_name

    def upload_file(self, file_path, s3_folder):
        try:
            file_name = os.path.basename(file_path)
            s3_key = f"{s3_folder}/{file_name}"

            self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
            s3_url = f"s3://{self.bucket_name}/{s3_key}"
            print(f"File uploaded to {s3_url}")
            return s3_url
        except Exception as e:
            print(f"Error uploading file: {e}")
            return None

class UploadManager:
    def __init__(self, upload_url):
        self.upload_url = upload_url

    def post_file(self, file_path, context):
        try:
            with open(file_path, 'rb') as f:
                encoder = MultipartEncoder(
                    fields={
                        'file': (os.path.basename(file_path), f, 'application/octet-stream'),
                        'context': context
                    }
                )

                response = requests.post(self.upload_url, data=encoder, headers={'Content-Type': encoder.content_type})

                if response.status_code == 200:
                    print("File successfully uploaded to the service")
                    return response.json()
                else:
                    print(f"Failed to upload file: {response.status_code}, {response.text}")
                    return None
        except Exception as e:
            print(f"Error posting file: {e}")
            return None

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    config = load_config('config.yaml')

    aws_access_key = config['aws_access_key']
    aws_secret_key = config['aws_secret_key']
    region_name = config['region_name']
    bucket_name = config['bucket_name']
    file_path = config['file_path']
    s3_folder = config['s3_folder']
    upload_url = config['upload_url']

    # Upload file to S3
    s3_uploader = S3Uploader(aws_access_key, aws_secret_key, region_name, bucket_name)
    s3_url = s3_uploader.upload_file(file_path, s3_folder)

    if s3_url:
        # Post file to the service
        upload_manager = UploadManager(upload_url)
        result = upload_manager.post_file(file_path, s3_folder)
        print(result)
