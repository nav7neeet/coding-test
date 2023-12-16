import sys
import boto3


def list_s3_objects(bucket_name):
    # Create an S3 client
    s3 = boto3.client("s3")

    s3_objects_list = []
    try:
        # List all objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Get object key
        for obj in response.get("Contents", []):
            if not obj["Key"].endswith("/"):
                s3_objects_list.append(obj["Key"])
        return s3_objects_list

    except Exception as e:
        sys.exit(f"Error: {e}")


def filter_text_objects(bucket_name, s3_objetcs):
    # Create an S3 client
    s3 = boto3.client("s3")
    text_objects = []

    for object in s3_objetcs:
        try:
            response = s3.get_object(Bucket=bucket_name, Key=object)

            # Read the file content line by line to find text objects
            content = response["Body"].read().decode("utf-8").split("\n")
            text_objects.append(object)

        except Exception as e:
            print(f"\nskip file=> {object}\n", e)

    return text_objects
