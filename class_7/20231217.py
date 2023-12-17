#python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# import secret key
# path/to/serviceaccount
cred = credentials.Certificate("C:/Users/SP513-52N/Documents/Python_2023Autumn/firebase_token.json")
# Initiate firebase
firebase_admin.initialize_app(cred)
# Initiate firestore
db = firestore.client()

# doc = {
#     "name":"Lennert",
#     "email":"lennertyen1226@gmail.com"
# }

# doc_ref = db.collection("Autumn_students").document("student011")

# doc_ref.set(doc)

# collection_ref = db.collection("Autumn2023_Students")
# collection_ref.add(doc)

# doc = {
#     "name":"Jaclyn",
#     "email":"jaclyn@gmail.com"
# }

# doc_ref = db.collection("Autumn_students").document("student02")

# doc_ref.set(doc)

# collection_name = "Autumn2023-Student"
# document_name = "Student01"
# doc_ref = db.collection(collection_name).document(document_name)

# path = "Autumn2023-Student/Student01"
# doc_ref = db.document(path)

# try:
#     doc = doc_ref.get()
#     doc_dict = doc.to_dict()
#     print("The content of the document is : {}".format(doc_dict()))
# except:
#     print("The reference of document is not exsist, please check the path is correct or not. {}".format(path))


# path = "Autumn_students"
# collection_ref = db.collection(path)
# docs = collection_ref.where("name", "==", "Jaclyn").get()
# for doc in docs:
#     print("The content of document is :{}".format(doc.to_dict()))
    
# path = "Autumn_students/student011"
# doc_ref = db.document(path)
# doc = {"birthday":"1226"}
# doc_ref.update(doc)

# contacts = {
#     "email":"lennertyen1226@gmail.com",
#     "phone":"0989931977"
# }
# doc = {
#     "contacts":contacts
# }
# doc_ref.update(doc)

# path = "Autumn_students/student011"
# doc_ref = db.document(path)
# doc = {
#     "contacts.email":"abc@gmail.com"
# }
# doc_ref.update(doc)


# path = "Autumn_students/student02"
# doc_ref = db.document(path)
# doc = {
#     "contacts.email":"niceday@gmail.com"
# }
# doc_ref.update(doc)

# def_ref = db.document(path)
# doc_ref.delete()

students_ref = db.collection("Autumn2023_Students")
docs = students_ref.get()
for doc in docs:
    doc.reference.delete()