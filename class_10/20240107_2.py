# class Car:
#     def __init__(self, color):
#         self.color = color
#         self.next = None

# def traverse(head):
#     ptr = head
#     while ptr != None:
#         print("The color of the car is {}.".format(ptr.color))
#         ptr = ptr.next
#     print("Finish traverse!")


# def traverse(head):
#     ptr = head
#     while True:
#         print("The color of the car is {}.".format(ptr.color))
#         if ptr.next == head:
#             break
#         ptr = ptr.next
#     print("Finish traverse!")


# red = Car("Red")
# blue = Car("Blue")
# black = Car("Black")
# pink = Car("Pink")


# head = black
# black.next = None

# red.next = blue
# pink.next = blue
# blue.next = red

# traverse(red)

class Car:
    def __init__ (self, color):
        self.color = color
        self.previous = None
        self.next = None

head = Car("blue")
