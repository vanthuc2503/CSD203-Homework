import time
class Node:
# Tạo class Node với data và nút đầu là None
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
# Tạo class SinglyLinkedList với nút đầu là None
    def __init__(self):
        self.head = None

# 1. add a node with value x  at the head of  a list
    def addToHead(self, x): # Thêm vào đầu linked list nút mới có giá trị x
        new_node = Node(x) # Khởi tạo nút mới
        new_node.next = self.head #Con trỏ của nút mới trỏ vào nút đầu
        self.head = new_node #Gán nút đầu cho nút mới

# 2. add a node with value x  at the tail of  a list
    def addToTail(self, x):
        new_node = Node(x)
        if not self.head: #Trường hợp không có head tức là nút trống
            new_node = self.head #Gán nút mới làm nút đầu
            return #Dừng phương thức addToTail ngay mà không chạy tiếp các bước tiếp theo
        current = self.head #Khởi tạo current là nút đầu
        while current.next:
            current = current.next #Cú pháp truy cập nút tiếp theo cho đến cuối cùng
        current.next = new_node #Gán vị trí của nút mới vào đuôi

# 3. add a node with value x  after the node p
    def addAfter(self, value, x):
        new_node = Node(x)
        current = self.head
        while current:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                return #Dừng phương thức addAfter ngay mà không thực hiện những câu lệnh tiếp theo
            current = current.next
        print(f"There is no node with value {value} in list")

# 4. traverse from head to tail and dislay info of all nodes in the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end = " --> ")
            current = current.next

        print("None")

# 5. delete the head and return its info
    def deleteFromHead(self):
        if not self.head:
            print("List has no element!")
            return None
        del_value = self.head.data
        self.head = self.head.next
        return del_value

# 6. delete the tail and return its info
    def deleteFromTail(self):
        if not self.head:
            print("List has no element!")
            return None
        if not self.head.next:
            del_value = self.head.data
            self.head = None
            return del_value
        current = self.head
        while current.next.next:
            current = current.next
        del_value = current.next.data
        current.next = None
        return del_value

# 7. delete the node after the node  p  and return its info
    def deleteAfter(self, p):
        if not self.head:
            print("There is no element in list!")
            return
        current = self.head
        while current:
            if current.data == p and current.next != None:
                del_value = current.next.data
                current.next = current.next.next
                return del_value
            elif current.data == p and current.next == None:
                print(f"There is no element after {p} in List!")
                return
            current = current.next
        print(f"There is no element with value {p} in List")
        return None

# 8. delele the first node whose info is equal to x
    def Del(self, x):
        if not self.head:
            print("There is no element in list!")
            return

        if self.head.data == x:
            del_value = self.head.data
            self.head = self.head.next
            return del_value

        current = self.head
        while current:
            if current.next.data == x:
                del_value = current.next.data
                current.next = current.next.next
                return del_value
            current = current.next
        print(f"There is no element value {x} in List")
        return None
# 9. search and return the reference to the first node having info x
    def search(self, x):
        current = self.head
        while current:
            if current.data == x:
                return current
            current = current.next
        print(f"There is no element value {x} in List")
        return None

# 10. count and return number of nodes in the list
    def Count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return f"The number of elements in List: {count}"

# 11. delete an i-th node on the list. Besure that such a node exists
    def Delete(self, i):
        if i < 0:
            print("Index must be larger or equal 0")
        if i == 0:
            return self.deleteFromHead()

        current = self.head
        for k in range(i - 1):
            if not current:
                print(f"Index {i} is out of List")
            current = current.next
        if not current.next or not current:
            print(f"Index {i} is out of List")

        del_value = current.next.data
        current.next = current.next.next
        return del_value

# 12. sort the list by ascending order of info
    def sort(self):
        if not self.head or not self.head.next:
            print("List is always sorted")
            return
        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

# 13. delete node p if it exists in the list
    def DEL(self, p):
        if not self.head:
            print("There is no element in List")
            return

        if self.head.data == p:
            del_value = self.head.data
            self.head = self.head.next
            return del_value

        current = self.head
        while current.next and current.next.data != p:
            current = current.next

        if not current.next:
            print(f"There is no node value {p} in List")
            return

        del_value = current.next.data
        current.next = current.next.next
        return del_value

# 14. create and return array containing info of all nodes in the list
    def toArray(self):
        if not self.head:
            print("There is no element in List!")
            return

        current = self.head
        Array = []
        while current:
            Array.append(current.data)
            current = current.next
        return Array

# 15. Merge two ordered singly linked lists of integers into one ordered list
    def merge_lists(self, list1, list2):
        result = SinglyLinkedList()
        current = result.head

        while list1 and list2:
            if list1.data < list2.data:
                if current is None:
                    result.head = Node(list1.data)
                    current = result.head
                else:
                    current.next = Node(list1.data)
                    current = current.next
                list1 = list1.next
            else:
                if current is None:
                    result.head = Node(list2.data)
                    current = result.head
                else:
                    current.next = Node(list2.data)
                    current = current.next
                list2 = list2.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return result

# 16. add a node with value x  before the node p
    def addBefore(self, p, x):
        if not self.head:
            print("There is no element in List!")

        current = self.head
        new_node = Node(x)
        if current.data == p:
            return self.addToHead()

        while current:
            while current.next.next:
                if current.next.data == p:
                    new_node.next = current.next
                    current.next = new_node
                current.next = current.next.next
            current = current.next
        print(f"There no node value {p} in List")

# 17. Attach a singly linked list to the end of another singly linked list
    def attach_lists(self, list1, list2):
        if not list1.head:
            list1.head = list2.head
        else:
            current = list1.head
            while current.next:
                current = current.next
            current.next = list2.head

# 18. find and return the maximum value in the list
    def max_value(self):
        if not self.head:
            print("There is no element in list!")
            return None

        max_val = self.head.data
        current = self.head.next

        while current:
            max_val = max(max_val, current.data)
            current = current.next

        return max_val

# 19. find and return the minimum value in the list
    def min_value(self):
        if not self.head:
            print("There is no element in List!")
            return None

        min_val = self.head.data
        current = self.head.next

        while current:
            min_val = min(min_val, current.data)
            current = current.next

        return min_val

# 20. return the average of all values in the list
    def list_sum(self):
        total = 0
        current = self.head

        while current:
            total += current.data
            current = current.next

        return total

# 21. return the average of all values in the list
    def list_avg(self):
        count = 0
        total = 0
        current = self.head

        while current:
            count += 1
            total += current.data
            current = current.next

        if count == 0:
            print("There is no element in List!")
            return None

        return total / count

# 22. check and return true if the list is sorted, return false if the list is not sorted
    def is_sorted(self):
        current = self.head

        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next

        return True

# 23. insert node with value x into sorted list so that the new list is sorted
    def insert(self, x):
        new_node = Node(x)

        if not self.head or x <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while current.next and current.next.data < x:
            current = current.next

        new_node.next = current.next
        current.next = new_node

# 24. Reverse a singly linked list using only one pass through the list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

# 25. Check whether two singly linked list have the same contents
    def check_equal(self, list1, list2):
        while list1 and list2:
            if list1.data != list2.data:
                return False
            list1 = list1.next
            list2 = list2.next

        return list1 is None and list2 is None

LinkedList = SinglyLinkedList()

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
        x = int(input("Enter the value of x: "))
        LinkedList.addToHead(x)
        LinkedList.traverse()

    elif choice == 2:
        x = int(input("Enter the value of x: "))
        LinkedList.addToTail(x)
        LinkedList.traverse()

    elif choice == 3:
        p = int(input("Enter the value of p: "))
        x = int(input("Enter the value of x: "))
        LinkedList.addAfter(p, x)
        LinkedList.traverse()

    elif choice == 4:
        LinkedList.traverse()

    elif choice == 5:
        deleted_value = LinkedList.deleteFromHead()
        print(f"Deleted node value: {deleted_value}")
        LinkedList.traverse()

    elif choice == 6:
        deleted_value = LinkedList.deleteFromTail()
        print(f"Deleted node value: {deleted_value}")
        LinkedList.traverse()

    elif choice == 7:
        p = int(input("Enter the value of p: "))
        deleted_value = LinkedList.deleteAfter(p)
        print(f"Deleted node value: {deleted_value}")
        LinkedList.traverse()

    elif choice == 8:
        x = int(input("Enter the value of x to delete: "))
        deleted_value = LinkedList.Del(x)
        print(f"Deleted node value: {deleted_value}")
        LinkedList.traverse()

    elif choice == 9:
        x = int(input("Enter the value to search: "))
        node_reference = LinkedList.search(x)
        if node_reference:
            print(f"Node found with value {x}")

    elif choice == 10:
        count = LinkedList.Count()
        print(count)

    elif choice == 11:
        i = int(input("Enter the index of the node to delete: "))
        deleted_value = LinkedList.Delete(i)
        print(f"Deleted node value: {deleted_value}")
        LinkedList.traverse()

    elif choice == 12:
        LinkedList.sort()
        LinkedList.traverse()

    elif choice == 13:
        p = int(input("Enter the value of p to delete: "))
        deleted_value = LinkedList.DEL(p)
        print(f"Deleted node value: {deleted_value}")
        LinkedList.traverse()

    elif choice == 14:
        array = LinkedList.toArray()
        print("Array:", array)

    elif choice == 15:
        # Assuming list1 and list2 are instances of SinglyLinkedList
        list1 = SinglyLinkedList()
        list2 = SinglyLinkedList()
        result = LinkedList.merge_lists(list1, list2)
        print("Merged List:")
        result.traverse()

    elif choice == 16:
        p = int(input("Enter the value of p: "))
        x = int(input("Enter the value of x: "))
        LinkedList.addBefore(p, x)
        LinkedList.traverse()

    elif choice == 17:
        # Assuming list1 and list2 are instances of SinglyLinkedList
        LinkedList.attach_lists(list1, list2)
        LinkedList.traverse()

    elif choice == 18:
        max_val = LinkedList.max_value()
        print(f"Maximum value in the list: {max_val}")

    elif choice == 19:
        min_val = LinkedList.min_value()
        print(f"Minimum value in the list: {min_val}")

    elif choice == 20:
        list_sum = LinkedList.list_sum()
        print(f"Sum of all values in the list: {list_sum}")

    elif choice == 21:
        list_avg = LinkedList.list_avg()
        print(f"Average of all values in the list: {list_avg}")

    elif choice == 22:
        is_sorted = LinkedList.is_sorted()
        print(f"Is the list sorted? {is_sorted}")

    elif choice == 23:
        x = int(input("Enter the value of x to insert: "))
        LinkedList.insert(x)
        LinkedList.traverse()

    elif choice == 24:
        LinkedList.reverse()
        LinkedList.traverse()

    elif choice == 25:
        # Assuming list1 and list2 are instances of SinglyLinkedList
        are_equal = LinkedList.check_equal(list1.head, list2.head)
        print(f"Are the two lists equal? {are_equal}")

    else:
        print("Invalid choice. Please enter a number between 1 and 25.")

    time.sleep(3)





















