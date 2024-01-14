import time
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAfter(self, p, x):
        current = self.head
        while current is not None and current.data != p:
            current = current.next
        if current is None:
            print(f"There is no node value {p} in List!.")
        else:
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node
            if current == self.tail:
                self.tail = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def deleteFromHead(self):
        if self.head is None:
            return None
        deleted_value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return deleted_value

    def deleteFromTail(self):
        if self.head is None:
            return None
        deleted_value = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        return deleted_value

    def deleteAfter(self, p):
        current = self.head
        while current is not None and current.data != p:
            current = current.next
        if current is None or current.next is None:
            print(f"There is no node value {p} in list or no node after it.")
        else:
            deleted_value = current.next.data
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            return deleted_value

    def delete(self, x):
        if self.head is None:
            return None
        if self.head.data == x:
            return self.deleteFromHead()
        current = self.head
        while current.next is not None and current.next.data != x:
            current = current.next
        if current.next is None:
            return None
        deleted_value = current.next.data
        current.next = current.next.next
        if current.next is None:
            self.tail = current
        return deleted_value

    def search(self, x):
        current = self.head
        while current is not None and current.data != x:
            current = current.next
        return current

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


linked_list = SinglyLinkedList()

while True:
    print("Menu:")
    print("1. add a node with value x  at the head of  a list ")
    print("2. add a node with value x  at the tail of  a list")
    print("3. add a node with value x  after the node p")
    print("4. traverse from head to tail and dislay info of all nodes in the list")
    print("5. delete the head and return its info")
    print("6. delete the tail and return its info")
    print("7. delete the node after the node  p  and return its info")
    print("8. delele the first node whose info is equal to x")
    print("9. search and return the reference to the first node having info x")
    print("10. count and return number of nodes in the list")

    choice = input("Enter your choice: ")

    if choice == '1':
        x = input("Enter value to add to head: ")
        linked_list.addToHead(x)
        linked_list.traverse()
    elif choice == '2':
        x = input("Enter value to add to tail: ")
        linked_list.addToTail(x)
        linked_list.traverse()
    elif choice == '3':
        p = input("Enter node value after which to add: ")
        x = input("Enter value to add: ")
        linked_list.addAfter(p, x)
        linked_list.traverse()
    elif choice == '4':
        print("Linked List:")
        linked_list.traverse()
        linked_list.traverse()
    elif choice == '5':
        deleted_value = linked_list.deleteFromHead()
        print(f"Deleted from head: {deleted_value}")
        linked_list.traverse()
    elif choice == '6':
        deleted_value = linked_list.deleteFromTail()
        print(f"Deleted from tail: {deleted_value}")
        linked_list.traverse()
    elif choice == '7':
        p = input("Enter node value after which to delete: ")
        deleted_value = linked_list.deleteAfter(p)
        print(f"Deleted after {p}: {deleted_value}")
        linked_list.traverse()
    elif choice == '8':
        x = input("Enter value to delete: ")
        deleted_value = linked_list.delete(x)
        if deleted_value is not None:
            print(f"Deleted: {deleted_value}")
        else:
            print(f"Node with value {x} not found.")
        linked_list.traverse()
    elif choice == '9':
        x = input("Enter value to search: ")
        node = linked_list.search(x)
        if node is not None:
            print(f"Node found: {node.data}")
        else:
            print(f"Node with value {x} not found.")
        linked_list.traverse()
    elif choice == '10':
        count = linked_list.count()
        print(f"Number of nodes in the list: {count}")
        linked_list.traverse()
    elif choice.lower() == 'e':
        break
    else:
        print("Invalid choice. Please try again.")

    time.sleep(3)
