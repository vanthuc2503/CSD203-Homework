class EmptyStackException(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("There is no element is stack!")
        value = self.head.value
        self.head = self.head.next
        return value

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("There is no element is stack!")
        return self.head.value

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end = " ")
            current = current.next
        print()

def decimal_to_binary(decimal_number):
    stack = Stack()
    decimal_number = int(decimal_number)
    while decimal_number > 0:
        remainder = decimal_number % 2
        stack.push(remainder)
        decimal_number //= 2

    binary_number = ""
    while not stack.isEmpty():
        binary_number += str(stack.pop())

    return binary_number

