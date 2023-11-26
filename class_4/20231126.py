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
'''
#sign up
def signup():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Successfully signup!")
    except:
        print("Email account has alreasy exist!")

def login():
    print("Log in...")
    email = input("Please enter your email: ")
    password = input("Please enert your password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print(login["localId"])
        print(login)
        print("Successfully logged in!")
    except:
        print("Invalid email or password!")
login()
'''
'''
class Car:
    def __init__(self, color):
        self.color = color
        self.next = None
head = Car("red")
head.next = None

def traverse(head):
    ptr = head
    while ptr != None:
        print("The color of the car is {}.".format(ptr.color))
        ptr = ptr.next
    print("Finish traverse!")

traverse(head)
'''

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.next = None
head = Student("Bob", 88)
head.next = None

def traverse(head):
    ptr = head
    while ptr != None:
        print("The student name is {} and the math  score is {}.".format(ptr.name, ptr.number))
        ptr = ptr.next
    print("Finish traverse!")

traverse(head)