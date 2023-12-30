#python
import pyrebase
from tkinter import *
config = {
    "apiKey": "AIzaSyCCuazXE1XoivXDdZ_5bfNXOeOaa0DD_yM",
    "authDomain": "fir-test-df8a5.firebaseapp.com",
    "projectId": "fir-test-df8a5",
    "storageBucket": "fir-test-df8a5.appspot.com",
    "messagingSenderId": "289290124982",
    "appId": "1:289290124982:web:e3a63485b1d4b42d26f017",
    "databaseURL" : ""
}

# Connect firebase and the python script by using app config
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

#初始化Tkinter
root = Tk()

loginlabel = Label(root, text = "Login Page")
accountlabel = Label(root, text = "Account")
passwordlabel = Label(root, text = "Password")
resultlabel = Label(root, text = "")

#創建帳號跟密把輸入框
accountentry = Entry(root)
#密碼輸入會顯示為星號
passwordentry = Entry(root, show="*")
signupbutton = Button(root, text = "Sign up", width = 10, command=lambda: adduser(root, accountentry, passwordentry))

#放置元件
loginlabel.pack(pady=5)
accountlabel.pack(pady=5)
passwordlabel.pack(pady=5)
resultlabel.pack(pady=5)
accountentry.pack(pady=5)
passwordentry.pack(pady=5)
signupbutton.pack(pady=5)

# 登入firebase
def adduser(view, accountentry, passwordentry):
    #取得使用者輸入的帳密，顯示在terminal
    print(accountentry.get(), passwordentry.get())
    print("Sign up...")
    #將帳號密碼處存到變數內
    account = accountentry.get()
    password = passwordentry.get()
    try:
        user = auth.create_user_with_email_and_password(account, password)
        print("Successfully sign up!")
        resultlabel.config(text="Successfully sign up!")
    except Exception as e:
        print(f"創建使用者失敗: {e}")
        resultlabel["text"] = "Create user failed!"
root.mainloop()


# class Car:
#     def __init__(self, color):
#         self.color = color
#         self.next = None
# head = Car("Red")
# head.next = None

# def traverse(head):
#     ptr = head
#     while ptr != None:
#         print("The color of the car is {}.".format(ptr.color))
#         ptr = ptr.next
#     print("Finish traverse!")

# newnode = Car("Blue")
# newnode.next = head
# head = newnode

# newnode2 = Car("Black")
# head.next.next = newnode2
# newnode2.next = None

# traverse(head)