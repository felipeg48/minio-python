import json
from datetime import datetime
from io import StringIO

import boto3

s3 = boto3.resource('s3',
  endpoint_url='http://127.0.0.1:9000',
  aws_access_key_id='minioadmin',
  aws_secret_access_key='minioadmin',
  config=boto3.session.Config(signature_version='s3v4')
)

object = s3.Object('test','simple')
curr_date = datetime.now().strftime("%Y%m%d-%H%M%S")

restore_data = {
            "filename": "somefile.tar",
            "creationDate": curr_date
        }
data = [
  restore_data
]

object.put(Body=json.dumps(data), ContentType='application/json')

print(object.get())
json = json.loads(object.get()['Body'].read())
print(json[0])