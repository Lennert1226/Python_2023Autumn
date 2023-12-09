#python
import pyrebase
config = {
    "apiKey": "AIzaSyCCuazXE1XoivXDdZ_5bfNXOeOaa0DD_yM",
    "authDomain": "fir-test-df8a5.firebaseapp.com",
    "projectId": "fir-test-df8a5",
    "storageBucket": "fir-test-df8a5.appspot.com",
    "messagingSenderId": "289290124982",
    "appId": "1:289290124982:web:e3a63485b1d4b42d26f017",
    "databaseURL" : ""
}

#
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()

def signup():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    user = auth.create_user_with_email_and_password(email, password)
    print("Successfully signup!")

def signup():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Successfully signup!")
    except:
        print("Email account has already exist!")

def login():
    print("Log in...")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
    except:
        print("Invalid email or password!")

login()