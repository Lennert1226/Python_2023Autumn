import os
import firebase_admin
from firebase_admin import credentials,storage
cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket':'fir-test-df8a5.appspot.com'})

# file_path = "ocean.jpg"
# bucket = storage.bucket()
# blob = bucket.blob(file_path)
# blob.upload_from_filename(file_path)

# def upload_blob(bucket, source_file_name, destination_blob_name):
#     blob = bucket.blob(destination_blob_name)
#     blob.upload_from_filename(source_file_name)
#     print(f"File {source_file_name} upload to {destination_blob_name}.")

# upload_blob(bucket, "ocean.jpg", "nature/beautiful_sea.jpg")



# dir_path = "./taipei"
# filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg")]
# print(filelist)

# bucket = storage.bucket()
# for file in filelist:
#     file_path = dir_path+"/"+file
#     blob_path = "taipei/"+file
#     print("Now is uploading file {}.".format(file_path))
#     blob = bucket.blob(blob_path)
#     blob.upload_from_filename(file_path)

bucket = storage.bucket()
blob = bucket.blob("nature/beautiful_sea.jpg")
blob.download_to_filename("my_love.jpg")