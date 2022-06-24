import json
from datetime import datetime
import boto3
import botocore


def s3_get_object(s3_resource, bucket, key):
    try:
        _object = s3_resource.Object(bucket, key)
        return _object.get()
    except botocore.errorfactory.ClientError as e:
        code = e.response['Error']['Code']
        if code == '404' or 'NoSuchKey':
            return None
        else:
            raise e


def s3_get_object_from_bucket_resource(bucket_resource, key):
    try:
        _object = bucket_resource.Object(key)
        return _object.get()
    except botocore.errorfactory.ClientError as e:
        code = e.response['Error']['Code']
        if code == '404' or 'NoSuchKey':
            return None
        else:
            raise e


s3 = boto3.resource('s3',
                    endpoint_url='http://127.0.0.1:9000',
                    aws_access_key_id='minioadmin',
                    aws_secret_access_key='minioadmin',
                    config=boto3.session.Config(signature_version='s3v4')
                    )

# object = s3.Object('test','simple2')
# curr_date = datetime.now().strftime("%Y%m%d-%H%M%S")
# restore_data = {
#             "filename": "somefile.tar",
#             "creationDate": curr_date
#         }
# data = [
#   restore_data
# ]

# object.put(Body=json.dumps(data), ContentType='application/json')
# object = s3_get_object(s3, 'test', 'simple2')

bucket = s3.Bucket("test")
object = s3_get_object_from_bucket_resource(bucket,'simple')

if object is None:
    print("Do something..")
else:
    print(json.loads(object['Body'].read()))
