import boto3
from django.conf import settings


def delete_image_from_s3(instance, image_field_name):
    image_field = getattr(instance, image_field_name)
    if image_field:
        s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
        bucket.delete_objects(Delete={'Objects': [{'Key': f'media/{image_field.name}'}]})

