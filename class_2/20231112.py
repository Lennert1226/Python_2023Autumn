#python

#import firebase packages
import firebase_admin
from firebase_admin import credentials

#引用套件auth
from firebase_admin import auth

#connect python with firebase private service key.
cred = credentials.Certificate("C:/Users/SP513-52N/Documents/Python_2023Autumn/fir-test-df8a5-firebase-adminsdk-h02nt-250b1fd8d8.json")
firebase_admin.initialize_app(cred)

email = "lennertyen0919@gmail.com"
password = "990919"
phone_number= "+886922403466"

user = auth.create_user(email = email, password = password, phone_number = phone_number)
print("User create successfully! {}".format(user.uid))