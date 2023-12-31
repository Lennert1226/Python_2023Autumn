#python
import os
import pyrebase
config = {
    "apiKey": "AIzaSyCCuazXE1XoivXDdZ_5bfNXOeOaa0DD_yM",
    "authDomain": "fir-test-df8a5.firebaseapp.com",
    "projectId": "fir-test-df8a5",
    "storageBucket": "fir-test-df8a5.appspot.com",
    "messagingSenderId": "289290124982",
    "appId": "1:289290124982:web:e3a63485b1d4b42d26f017",
    "databaseURL" : "",
    "serviceAccount":"../firebase_token.json"
}

#
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

dir_name = "nature"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

storage = firebase.storage()
all_files = storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name):
        file.download_to_filename(file.name)

