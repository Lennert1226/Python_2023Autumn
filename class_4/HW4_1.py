class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
head = Employee("Amy", 25)
head.next = None

def traverse(head):
    ptr = head
    while ptr != None:
        print("The employee name is {} and the age is {}.".format(ptr.name, ptr.age))
        ptr = ptr.next
    print("Finish traverse!")

traverse(head)