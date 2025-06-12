import boto3

s3 = boto3.client("s3") #Reference to S3  - used for every operation

BUCKET_NAME = "dummy-youtube-comments-bucket"

# # To check the region
# session = boto3.session.Session()
# print(session.region_name)

#Create Bucket
bucket_location = s3.create_bucket(
    Bucket = BUCKET_NAME,
    CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
)
print(bucket_location)

#Upload json dataset of dummy yt comments into the bucket
FILE_PATH = "./data/dummy_comments_yt.json"
FOLDER_NAME = "raw"
FILE_NAME = "dummy_comments_youtube"
with open(FILE_PATH,"rb") as f: #rb is read mode
    # s3.upload_fileobj(
    #     f, BUCKET_NAME, "burger_new_upload.jpg")
    s3.upload_fileobj(
        f, BUCKET_NAME, f"{FOLDER_NAME}/{FILE_NAME}") #opens json file and uploads it under "folder" raw
    

#Upload Confirmation
print(f"Uploaded {FILE_PATH} to {bucket_location}")

