import time
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def addAfter(self, p, x):
        new_node = Node(x)
        temp = self.head
        while temp.data != p:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def traverse(self):
        if not self.head:
            print("List is empty")
        else:
            temp = self.head
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print()

    def deleteFromHead(self):
        if not self.head:
            return None
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            data = self.head.data
            temp.next = self.head.next
            self.head = self.head.next
            return data

    def deleteFromTail(self):
        if not self.head:
            return None
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            data = temp.data
            prev.next = self.head
            return data

    def deleteAfter(self, p):
        temp = self.head
        while temp.data != p:
            temp = temp.next
        data = temp.next.data
        temp.next = temp.next.next
        return data

    def delete(self, x):
        if not self.head:
            return None
        if self.head.data == x:
            return self.deleteFromHead()
        temp = self.head
        while temp.next != self.head and temp.next.data != x:
            temp = temp.next
        if temp.next.data == x:
            data = temp.next.data
            temp.next = temp.next.next
            return data
        return None

    def search(self, x):
        if not self.head:
            return None
        temp = self.head
        while temp.data != x:
            temp = temp.next
            if temp == self.head:
                return None
        return temp

    def count(self):
        count = 0
        temp = self.head
        if temp:
            while True:
                count += 1
                temp = temp.next
                if temp == self.head:
                    break
        return count

    def deleteAt(self, i):
        if not self.head or i <= 0:
            return None
        if i == 1:
            return self.deleteFromHead()
        temp = self.head
        for _ in range(i - 2):
            temp = temp.next
            if temp == self.head:
                return None
        data = temp.next.data
        temp.next = temp.next.next
        return data

    def sort(self):
        if not self.head:
            return
        temp1 = self.head
        while temp1.next != self.head:
            temp2 = temp1.next
            while temp2 != self.head:
                if temp2.data < temp1.data:
                    temp1.data, temp2.data = temp2.data, temp1.data
                temp2 = temp2.next
            temp1 = temp1.next

    def delNode(self, p):
        if not self.head:
            print("List is empty")
            return

        if self.head.data == p:
            self.head = self.head.next
            print(f"Node with value {p} deleted")
            return

        temp = self.head
        prev = None

        while temp and temp.data != p:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
            print(f"Node with value {p} deleted")
        else:
            print(f"Node with value {p} not found")

    def toArray(self):
        arr = []
        temp = self.head
        if temp:
            while True:
                arr.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        return arr

    def merge(self, other_list):
        if not other_list.head:
            return
        temp = other_list.head
        while True:
            self.addToTail(temp.data)
            temp = temp.next
            if temp == other_list.head:
                break

    def addBefore(self, p, x):
        new_node = Node(x)
        temp = self.head
        while temp.next != self.head and temp.next.data != p:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        if p == self.head.data:
            self.head = new_node

    def attachList(self, other_list):
        if not other_list.head:
            return

        if not self.head:
            self.head = other_list.head
            current = self.head
            while current.next != other_list.head:
                current = current.next
            current.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = other_list.head
            current = other_list.head
            while current.next != other_list.head:
                current = current.next
            current.next = self.head

    def max(self):
        if not self.head:
            return None
        current = self.head
        max_value = current.data
        while True:
            current = current.next
            if current == self.head:
                break
            if current.data > max_value:
                max_value = current.data
        return max_value

    def min(self):
        if not self.head:
            return None
        current = self.head
        min_value = current.data
        while True:
            current = current.next
            if current == self.head:
                break
            if current.data < min_value:
                min_value = current.data
        return min_value

    def sum(self):
        if not self.head:
            return 0
        current = self.head
        total_sum = current.data
        while True:
            current = current.next
            if current == self.head:
                break
            total_sum += current.data
        return total_sum

    def avg(self):
        count = 0
        total_sum = 0
        current = self.head
        while True:
            count += 1
            total_sum += current.data
            current = current.next
            if current == self.head:
                break
        if count == 0:
            return None
        return total_sum / count

    def sorted(self):
        current = self.head
        while True:
            if current.data > current.next.data:
                return False
            current = current.next
            if current == self.head:
                break
        return True

    def insert(self, x):
        new_node = Node(x)
        if not self.head or x <= self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head and x > current.next.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head = prev

    def same_contents(self, other_list):
        current_self = self.head
        current_other = other_list.head

        while True:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next

            if current_self == self.head and current_other == other_list.head:
                break

        return True


circular_linked_list = CircularLinkedList()

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
    choice = int(input("Enter your choice (0 to exit): "))

    if choice == 0:
        break
    elif choice == 1:
        data = int(input("Enter the value to add to the head: "))
        circular_linked_list.addToHead(data)
        circular_linked_list.traverse()
    elif choice == 2:
        data = int(input("Enter the value to add to the tail: "))
        circular_linked_list.addToTail(data)
        circular_linked_list.traverse()
    elif choice == 3:
        p = int(input("Enter the value after which to add a new node: "))
        data = int(input("Enter the value of the new node: "))
        circular_linked_list.addAfter(p, data)
        circular_linked_list.traverse()
    elif choice == 4:
        circular_linked_list.traverse()
    elif choice == 5:
        circular_linked_list.deleteFromHead()
        circular_linked_list.traverse()
    elif choice == 6:
        circular_linked_list.deleteFromTail()
        circular_linked_list.traverse()
    elif choice == 7:
        p = int(input("Enter the value after which to delete the node: "))
        circular_linked_list.deleteAfter(p)
        circular_linked_list.traverse()
    elif choice == 8:
        p = int(input("Enter the value of the node to delete: "))
        circular_linked_list.delNode(p)
        circular_linked_list.traverse()
    elif choice == 9:
        x = int(input("Enter the value to search for: "))
        node = circular_linked_list.search(x)
        if node:
            print(f"Node with value {x} found.")
        else:
            print(f"Node with value {x} not found.")
    elif choice == 10:
        count = circular_linked_list.count()
        print(f"Number of nodes in the list: {count}")
    elif choice == 11:
        i = int(input("Enter the position to delete: "))
        circular_linked_list.deleteAt(i)
        circular_linked_list.traverse()
    elif choice == 12:
        circular_linked_list.sort()
        circular_linked_list.traverse()
    elif choice == 13:
        x = int(input("Enter the value to delete: "))
        circular_linked_list.delete(x)
        circular_linked_list.traverse()
    elif choice == 14:
        arr = circular_linked_list.toArray()
        print("Linked List as Array:", arr)
    elif choice == 15:
        other_list = CircularLinkedList()
        data = int(input("Enter the value for the other list: "))
        other_list.addToTail(data)
        circular_linked_list.merge(other_list)
    elif choice == 16:
        p = int(input("Enter the value after which to add a new node: "))
        data = int(input("Enter the value of the new node: "))
        circular_linked_list.addBefore(p, data)
    elif choice == 17:
        other_list = CircularLinkedList()
        data = int(input("Enter the value for the other list: "))
        other_list.addToTail(data)
        circular_linked_list.attachList(other_list)
    elif choice == 18:
        max_value = circular_linked_list.max()
        print(f"Maximum value in the list: {max_value}")
    elif choice == 19:
        min_value = circular_linked_list.min()
        print(f"Minimum value in the list: {min_value}")
    elif choice == 20:
        total_sum = circular_linked_list.sum()
        print(f"Sum of all values in the list: {total_sum}")
    elif choice == 21:
        average = circular_linked_list.avg()
        print(f"Average of all values in the list: {average}")
    elif choice == 22:
        is_sorted = circular_linked_list.sorted()
        if is_sorted:
            print("The list is sorted.")
        else:
            print("The list is not sorted.")
        circular_linked_list.traverse()
    elif choice == 23:
        x = int(input("Enter the value to insert into the sorted list: "))
        circular_linked_list.insert(x)
        circular_linked_list.traverse()
    elif choice == 24:
        circular_linked_list.reverse()
        circular_linked_list.traverse()
    elif choice == 25:
        other_list = CircularLinkedList()
        data = int(input("Enter the value for the other list: "))
        other_list.addToTail(data)
        are_same = circular_linked_list.same_contents(other_list)
        if are_same:
            print("The lists have the same contents.")
        else:
            print("The lists do not have the same contents.")
        circular_linked_list.traverse()
    time.sleep(3)
