import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addAfter(self, p, x):
        current = self.head
        while current is not None and current.data != p:
            current = current.next
        if current is None:
            print(f"Node with value {p} not found.")
        else:
            new_node = Node(x)
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            if current == self.tail:
                self.tail = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def deleteFromHead(self):
        if self.head is None:
            return None
        deleted_value = self.head.data
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return deleted_value

    def deleteFromTail(self):
        if self.tail is None:
            return None
        deleted_value = self.tail.data
        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        return deleted_value

    def deleteAfter(self, p):
        current = self.head
        while current is not None and current.data != p:
            current = current.next
        if current is None or current.next is None:
            print(f"Node with value {p} not found or no node after it.")
        else:
            deleted_value = current.next.data
            current.next = current.next.next
            if current.next is not None:
                current.next.prev = current
            if current.next is None:
                self.tail = current
            return deleted_value

    def delete(self, x):
        current = self.head
        while current is not None and current.data != x:
            current = current.next
        if current is None:
            return None
        deleted_value = current.data
        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
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

    def delAtIndex(self, i):
        current = self.head
        for _ in range(i):
            if current is None:
                print(f"Node at index {i} does not exist.")
                return
            current = current.next
        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

    def sort(self):
        values = self.toArray()
        values.sort()
        self.head = self.tail = None
        for value in values:
            self.addToTail(value)

    def delNode(self, p):
        current = self.head
        while current is not None and current.data != p:
            current = current.next
        if current is None:
            print(f"Node with value {p} not found.")
        else:
            if current.prev is not None:
                current.prev.next = current.next
            else:
                self.head = current.next
            if current.next is not None:
                current.next.prev = current.prev
            else:
                self.tail = current.prev

    def toArray(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def mergeOrderedLists(self, other_list):
        merged_list = DoublyLinkedList()
        current1, current2 = self.head, other_list.head

        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                merged_list.addToTail(current1.data)
                current1 = current1.next
            else:
                merged_list.addToTail(current2.data)
                current2 = current2.next

        while current1 is not None:
            merged_list.addToTail(current1.data)
            current1 = current1.next

        while current2 is not None:
            merged_list.addToTail(current2.data)
            current2 = current2.next

        return merged_list

    def addBefore(self, p, x):
        current = self.head
        while current is not None and current.data != p:
            current = current.next
        if current is None:
            print(f"Node with value {p} not found.")
        else:
            new_node = Node(x)
            new_node.prev = current.prev
            new_node.next = current
            if current.prev is not None:
                current.prev.next = new_node
            else:
                self.head = new_node
            current.prev = new_node

    def attachList(self, other_list):
        if self.tail is not None:
            self.tail.next = other_list.head
            if other_list.head is not None:
                other_list.head.prev = self.tail
            self.tail = other_list.tail
        else:
            self.head = other_list.head
            self.tail = other_list.tail

    def max(self):
        if self.head is None:
            return None
        current = self.head
        max_value = current.data
        while current is not None:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def min(self):
        if self.head is None:
            return None
        current = self.head
        min_value = current.data
        while current is not None:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

    def sum(self):
        current = self.head
        total_sum = 0
        while current is not None:
            total_sum += current.data
            current = current.next
        return total_sum

    def avg(self):
        if self.head is None:
            return None
        current = self.head
        total_sum = 0
        count = 0
        while current:
            total_sum += current.data
            count += 1
            current = current.next
        return total_sum / count

    def sorted(self):
        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def insert(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
        elif x <= self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif x >= self.tail.data:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next.data < x:
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def reverse_doubly_linked_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def same_contents(list1, list2):
        current1, current2 = list1.head, list2.head
        while current1 and current2:
            if current1.data != current2.data:
                return False
            current1, current2 = current1.next, current2.next
        return current1 is None and current2 is None


doubly_linked_list = DoublyLinkedList()
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
    print("11. delete an i-th node on the list. Besure that such a node exists")
    print("12. sort the list by ascending order of info")
    print("13. delete node p if it exists in the list")
    print("14. create and return array containing info of all nodes in the list")
    print("15. Merge two ordered singly linked lists of integers into one ordered list.")
    print("16. add a node with value x  before the node p")
    print("17. Attach a singly linked list to the end of another singly linked list")
    print("18. find and return the maximum value in the list")
    print("19. find and return the minimum value in the list")
    print("20. return the sum of all values in the list")
    print("21. return the average of all values in the list")
    print("22. check and return true if the list is sorted, return false if the list is not sorted")
    print("23. insert node with value x into sorted list so that the new list is sorted")
    print("24. Reverse a singly linked list using only one pass through the list")
    print("25. Check whether two singly linked list have the same contents")

    choice = input("Choose program to run (1-25) or 'e' to exit: ")
    if choice == 'e':
        break
    choice = int(choice)
    if choice == 1:
        x = input("Enter value to add to head: ")
        doubly_linked_list.addToHead(x)
        doubly_linked_list.traverse()
    elif choice == 2:
        x = input("Enter value to add to tail: ")
        doubly_linked_list.addToTail(x)
        doubly_linked_list.traverse()
    elif choice == 3:
        p = input("Enter node value after which to add: ")
        x = input("Enter value to add: ")
        doubly_linked_list.addAfter(p, x)
        doubly_linked_list.traverse()
    elif choice == 4:
        print("Doubly Linked List:")
        doubly_linked_list.traverse()
    elif choice == 5:
        deleted_value = doubly_linked_list.deleteFromHead()
        print(f"Deleted from head: {deleted_value}")
        doubly_linked_list.traverse()
    elif choice == 6:
        deleted_value = doubly_linked_list.deleteFromTail()
        print(f"Deleted from tail: {deleted_value}")
        doubly_linked_list.traverse()
    elif choice == 7:
        p = input("Enter node value after which to delete: ")
        deleted_value = doubly_linked_list.deleteAfter(p)
        print(f"Deleted after {p}: {deleted_value}")
        doubly_linked_list.traverse()
    elif choice == 8:
        x = input("Enter value to delete: ")
        deleted_value = doubly_linked_list.delete(x)
        if deleted_value is not None:
            print(f"Deleted: {deleted_value}")
        else:
            print(f"Node with value {x} not found.")
        doubly_linked_list.traverse()
    elif choice == 9:
        x = input("Enter value to search: ")
        node = doubly_linked_list.search(x)
        if node is not None:
            print(f"Node found: {node.data}")
        else:
            print(f"Node with value {x} not found.")
        doubly_linked_list.traverse()
    elif choice == 10:
        count = doubly_linked_list.count()
        print(f"Number of nodes in the list: {count}")
        doubly_linked_list.traverse()
    elif choice == 11:
        i = int(input("Enter index to delete: "))
        doubly_linked_list.delAtIndex(i)
        doubly_linked_list.traverse()
    elif choice == 12:
        doubly_linked_list.sort()
        print("List sorted.")
        doubly_linked_list.traverse()
    elif choice == 13:
        p = input("Enter value of the node to delete: ")
        doubly_linked_list.delNode(p)
        doubly_linked_list.traverse()
    elif choice == 14:
        array_representation = doubly_linked_list.toArray()
        print(f"Array Representation: {array_representation}")
        doubly_linked_list.traverse()
    elif choice == 15:
        other_list = DoublyLinkedList()
        other_list.addToTail(4)
        other_list.addToTail(8)
        other_list.addToTail(12)
        merged_list = doubly_linked_list.mergeOrderedLists(other_list)
        print("Merged Ordered Lists:")
        merged_list.traverse()
    elif choice == 16:
        p = input("Enter node value before which to add: ")
        x = input("Enter value to add: ")
        doubly_linked_list.addBefore(p, x)
        doubly_linked_list.traverse()
    elif choice == 17:
        other_list = DoublyLinkedList()
        other_list.addToTail(21)
        other_list.addToTail(42)
        other_list.addToTail(63)
        doubly_linked_list.attachList(other_list)
        print("Lists Attached.")
        doubly_linked_list.traverse()
    elif choice == 18:
        max_value = doubly_linked_list.max()
        print(f"Maximum Value: {max_value}")
    elif choice == 19:
        min_value = doubly_linked_list.min()
        print(f"Minimum Value: {min_value}")
    elif choice == 20:
        sum_value = doubly_linked_list.sum()
        print(f"Sum of Values: {sum_value}")
    elif choice == 21:
        avg_value = doubly_linked_list.avg()
        print(f"Average of Values: {avg_value}")
    elif choice == 22:
        is_sorted = doubly_linked_list.sorted()
        print(f"Is List Sorted: {is_sorted}")
    elif choice == 23:
        x = int(input("Enter value to insert into sorted list: "))
        doubly_linked_list.insert(x)
        print(f"{x} inserted into the sorted list.")
    elif choice == 24:
        doubly_linked_list = Node(1)
        doubly_linked_list.next = Node(2)
        doubly_linked_list.next.next = Node(3)
        reversed_list = reverse_doubly_linked_list(doubly_linked_list)
        print("\nReversed Doubly Linked List:")
        while reversed_list:
            print(reversed_list.data, end=" -> ")
            reversed_list = reversed_list.next
        print("None")

    elif choice == 25:
        other_list = DoublyLinkedList()
        other_list.addToTail(1)
        other_list.addToTail(2)
        other_list.addToTail(3)
        are_same = same_contents(doubly_linked_list, other_list)
        print(f"Same contents: {are_same}")

    elif choice == 'e':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
    time.sleep(3)
