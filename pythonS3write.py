import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='',
aws_secret_access_key='/'
)

sts = boto3.client('sts')
print(sts.get_caller_identity())

#Creating S3 Resource From the Session.
s3 = session.resource('s3')
txt_data = b'SAMPLE DATA'

#write to S3
object = s3.Object('<bucket-name>', '<folder-name>/cust_data3.csv')

result = object.put(Body=txt_data)