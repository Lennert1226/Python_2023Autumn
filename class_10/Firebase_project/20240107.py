import firebase_admin
from firebase_admin import credentials,storage

import os
cred = credentials.Certificate("../../firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket':'fir-test-df8a5.appspot.com'})

dir_path = "./image"
filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg") or f.endswith(".png")]
print(filelist)

bucket = storage.bucket()
for file in filelist:
    file_path = dir_path+"/"+file
    blob_path = "project_images/"+file
    print("Now is uploading file {}.".format(file_path))
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)