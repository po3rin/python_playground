import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('kodansha-epub')
for object in bucket.objects.all():
    print(object.key)
    s3.Object(object.bucket_name, object.key).download_file('./data/' + object.key)
    # object.download_file('./data/' + object.key)
