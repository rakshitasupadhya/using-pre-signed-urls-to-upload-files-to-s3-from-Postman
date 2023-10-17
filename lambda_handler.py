import json
import boto3
import random

s3 = boto3.client('s3')
uploadBucket = 'bucket-touploadfile'
URL_EXPIRATION_SECONDS = 30000

def lambda_handler(event, context):
    return getUploadURL(event)

def getUploadURL(event):
    randomID = int(random.random() * 10000000)
    Key = f"{randomID}.jpeg"

    s3Params = {
        'Bucket': uploadBucket,
        'Key': Key,
        'Expires': URL_EXPIRATION_SECONDS,
        'ContentType': 'image/jpeg'
    }

    uploadURL = s3.generate_presigned_url('put_object', Params=s3Params)
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "uploadURL": uploadURL,
            "filename": Key
        })
    }
