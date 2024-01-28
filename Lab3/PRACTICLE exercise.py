#1
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
#2
def findmin(a, n):
    if n == 1:
        return a[0]
    rest = findmin(a[1:], n - 1)
    if a[0] < rest:
        return a[0]
    else:
        return rest


# a = [2, 10, 5, 3, 0, 5]
# n = len(a)
# minE = findmin(a, n)
# print(minE)

#3
def findsum(a, n):
    if n == 1:
        return a[0]
    else:
        return a[0] + findsum(a[1:], n - 1)


# a = [8, 20, 4, 23, 2, 5]
# n = len(a)
# total = findsum(a, n)
# print(total)

#4
def is_palindrome(a, n):
    if n <= 1:
        return True
    return a[0] == a[n - 1] and is_palindrome(a[1:n - 1], n - 2)

# arr = [1, 2, 3, 2, 1]
# size = len(arr)
#
# result = is_palindrome(arr, size)
#
# if result:
#     print("The array is a palindrome.")
# else:
#     print("The array is not a palindrome.")


#5
def search(a, n, target):
    if n > 0:
        if a[0] == target:
            return True
        else:
            return search(a[1:], n - 1, target)
    else:
        return False

#6
def GCD(m, n):
    if n == 0:
        return m
    elif n > 0:
        return GCD(n, m % n)

#7
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


#8
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

#9
def fibonacci(n):
    if n <= 0:
        print("Incorrect input")

    elif n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#10
def addReciprocals(n):
    if n == 0:
        print("Incorrect input")
    elif n == 1:
        return 1
    else:
        return 1 / n + addReciprocals(n - 1)


#11
def Stirlingnumb(n, k):
    if n == k == 0:
        return 1
    elif n > 0 and k == 0:
        return 0
    elif n == 0 or k > n:
        return 0
    return Stirlingnumb(n - 1, k - 1) - n * Stirlingnumb(n - 1, k)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#12
def tree_height(root):
    if root is None:
        return 0
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        return 1 + max(left_height, right_height)

#13
def tree_size(root):
    if root is None:
        return 0

    else:
        left_size = tree_size(root.left)
        right_size = tree_size(root.right)
        return 1 + left_size + right_size


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right = TreeNode(4)
# root.left.right = TreeNode(5)

# height = tree_height(root)
# size = tree_size(root)

# print("Height of binary tree: ", height)
# print("Size of binary tree: ", size)









