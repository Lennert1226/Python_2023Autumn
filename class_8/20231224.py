import firebase_admin
from firebase_admin import credentials,storage
cred = credentials.Certificate("../firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket':'fir-test-df8a5.appspot.com'})

file_path = "Firebase_project/image/bed1.jpg"
bucket = storage.bucket()
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)