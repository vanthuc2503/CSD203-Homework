from Lab2_Q1 import Stack
from  Lab2_Q1 import decimal_to_binary

stack_char = Stack()

print("Is stack empty?", stack_char.isEmpty() )

n = int(input("Enter the number of element "))
for i in range(n):
    while True:
        element = input(f"Enter element {i+1} (Remember that it contains only one character): ")
        if len(element) == 1:
            break
        else:
            print("Element must have only one character!")
    stack_char.push(element)

print("Stack after push: ")
stack_char.traverse()

print("Is stack empty?", stack_char.isEmpty() )

print("The element is pop: ",stack_char.pop())
print("Stack after pop: ")
stack_char.traverse()

print("The top element: ", stack_char.top())

stack_char.clear()
print("Stack after clear: ")
stack_char.traverse()

while True:
    decimal_number = input("Enter a decimal number: ")
    if decimal_number.isdecimal():
        break
    else:
        print("Please enter a decimal number!")

binary_number = decimal_to_binary(decimal_number)
print(f"The binary number of {decimal_number} is {binary_number}")

print()
print()

from Lab2_Q2 import Queue
from Lab2_Q2 import convert_real_number

queue_str = Queue()
print("Is queue empty? ", queue_str.isEmpty())

n = int(input("Enter the number of element "))
for i in range(n):
    while True:
        element = input(f"Enter element {i+1} (Remember that it contains only one character): ")
        if len(element) == 1:
            break
        else:
            print("Element must have only one character!")
    queue_str.enqueue(element)

print("Queue after enqueue: ")
queue_str.traverse()

print("Is queue empty? ", queue_str.isEmpty())

queue_str.dequeue()
print("Queue after dequeue 1 time: ")
queue_str.traverse()

print("First element: ", queue_str.first())

print("Clear queue")
queue_str.clear()
print("Is queue empty? ", queue_str.isEmpty())

number = float(input("Enter a real number in range [0; 1): "))
result = convert_real_number(number)
print("The binary number of that number is ")
result.traverse()

