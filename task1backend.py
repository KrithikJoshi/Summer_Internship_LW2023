#!/usr/bin//python3

import cgi
import boto3


print("Content-type: text/html")
print()

mydata = cgi.FieldStorage("n")
data = mydata.getvalue()
myname = data

create_bucket():
    bucket = boto3.client('s3',region_name='ap-south-1')
    bucket.create_bucket(
    Bucket='hsd5f5yk97do8',
    ACL='private',
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
    )
