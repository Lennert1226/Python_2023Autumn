class Car:
    def __init__(self, color):
        self.color = color
        self.next = None

def traverse(head):
    ptr = head
    while True:
        print("The color of the car is {}.".format(ptr.color))
        if ptr.next == head:
            break
        ptr = ptr.next
    print("Finish traverse!")

head = Car("Red")
blue = Car("Blue")
black = Car("Black")

head.next = blue
blue.next = head
black.next = head



ptr = head

while ptr.next != head:
    ptr =ptr.next
ptr.next = black

head = black

traverse(head)