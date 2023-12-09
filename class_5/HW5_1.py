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