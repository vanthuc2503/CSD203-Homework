class EmptyStackException(Exception):
    pass
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise EmptyStackException("Stack is empty")

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise EmptyStackException("Stack is empty")

    def traverse(self):
        for item in reversed(self.items):
            print(item.name, end=' ')

class EmptyQueueException(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise EmptyQueueException("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise EmptyQueueException("Queue is empty")

    def traverse(self):
        for item in self.items:
            print(item.name, end=' ')

class Car:
    def __init__(self, name):
        self.name = name

stack_car = Stack()
print("Is stack empty? ", stack_car.isEmpty())

while True:
    n = input("Enter the number of cars: ")
    if n.isdecimal():
        break
    else:
        print("Please enter a number please!")

for i in range(int(n)):
    name = input(f"Enter name of car {i+1}: ")
    stack_car.push(Car(name))

print("Stack of car after push is")
stack_car.traverse()
print()
print("Is stack empty? ", stack_car.isEmpty())

print("The element is pop: ",stack_car.pop().name)
print("Stack after pop: ")
stack_car.traverse()
print()
print("The top element: ", stack_car.top().name)

stack_car.clear()
print("Stack after clear: ")
stack_car.traverse()

print("Is stack empty? ", stack_car.isEmpty())

print()
print()
#Queue usage
queue_car = Queue()
print("Is queue empty? ", queue_car.is_empty())

while True:
    n = input("Enter the number of cars: ")
    if n.isdecimal():
        break
    else:
        print("Please enter a number!")

for i in range(int(n)):
    name = input(f"Enter name of car {i+1}: ")
    queue_car.enqueue(Car(name))

print("Queue of cars after enqueue is")
queue_car.traverse()
print()
print("Is queue empty? ", queue_car.is_empty())

print("The element is dequeue: ", queue_car.dequeue().name)
print("Queue after dequeue: ")
queue_car.traverse()
print()
print("Is queue empty? ", queue_car.is_empty())

queue_car.clear()
print("Queue after clear: ")
queue_car.traverse()
print()
print("Is queue empty? ", queue_car.is_empty())