# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.next = None
# head = Employee("Amy", 25)
# head.next = 

# newnode = Employee("Eddy", 43)
# newnode.next = 

# def traverse(head):
#     ptr = head
#     while ptr != None:
#         print("The student name is {} and the math  score is {}.".format(ptr.name, ptr.age))
#         ptr = ptr.next
#     print("Finish traverse!")

# traverse(head)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
head = Employee("Eddy", 43)
head.next = None

def traverse(head):
    ptr = head
    while ptr != None:
        print("The employee name is {} and the age is {}.".format(ptr.name, ptr.age))
        ptr = ptr.next
    print("Finish traverse!")

newnode = Employee("Amy", 25)
newnode.next = head
head = newnode

newnode2 = Employee("Esme", 32)
head.next.next = newnode2
newnode2.next = None

traverse(head)