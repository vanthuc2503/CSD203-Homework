class Exception(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def clear(self):
        self.front = self.rear = None

    def enqueue(self, x):
        new_node = Node(x)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("There is no element in queue!")
        else:
            value = self.front.value
            self.front = self.front.next
        return value

    def first(self):
        if self.isEmpty():
            raise Exception("There is no element in queue!")
        else:
            return self.front.value

    def traverse(self):
        current = self.front
        while current:
            print(current.value, end = " ")
            current = current.next
        print()

def convert_real_number(number):
    if not (0 <= number < 1):
        raise ValueError("Input must be a real number less than 1 and larger or equal than 0.")

    binary_queue = Queue()
    while number > 0:
        number *= 2
        bit = int(number)
        binary_queue.enqueue(bit)
        number -= bit

    return binary_queue

