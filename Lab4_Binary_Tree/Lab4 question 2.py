class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Binarysearchtree:
    def __init__(self):
        self.root = None
#1
    def isEmpty(self):
        return self.root is None
#2
    def clear(self):
        self.root = None
#3
    def search(self, x):
        return self._search(self.root, x)

    def _search(self, node, x):
        if node is None or node.key == x:
            return node
        if x < node.key:
            return self._search(node.left, x)
        else:
            return self._search(node.right, x)
#4
    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if node is None:
            return Node(x)
        if x < node.key:
            node.left = self._insert(node.left, x)
        elif x > node.key:
            node.right = self._insert(node.right, x)
        return node
#5
    def breadth(self):
        if self.root is None:
            return []
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
#6
    def preorder(self, p):
        if p:
            print(p.key, end=', ')
            self.preorder(p.left)
            self.preorder(p.right)
#7
    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.key, end=', ')
            self.inorder(p.right)
#8
    def postorder(self, p):
        if p:
            self.postorder(p.left)
            self.postorder(p.right)
            print(p.key, end=', ')
#9
    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)
#10
    def dele(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, root, x):
        if root is None:
            return root
        if x < root.key:
            root.left = self._delete(root.left, x)
        elif x > root.key:
            root.right = self._delete(root.right, x)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._minValueNode(root.right)
            root.right = self._delete(root.right, root.key)
        return root
#11
    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key

    def min(self):
        return self._min(self.root)

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node.key
#12
    def max(self):
        return self._max(self.root)

    def _max(self, node):
        while node.right is not None:
            node = node.right
        return node.key
#13
    def sum(self):
        return self._sum(self.root)

    def _sum(self, node):
        if node is None:
            return 0
        return len(node.key) + self._sum(node.left) + self._sum(node.right)
#14
    def avg(self):
        count = self.count()
        if count == 0:
            return 0
        return self.sum() / count
#15
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1
#16
    def cost_of_most_expensive_path(self):
        return self._cost_of_most_expensive_path(self.root)

    def _cost_of_most_expensive_path(self, node):
        if node is None:
            return 0
        left_cost = self._cost_of_most_expensive_path(node.left)
        right_cost = self._cost_of_most_expensive_path(node.right)
        return len(node.key) + max(left_cost, right_cost)
#17
    def is_avl(self):
        return self._is_avl(self.root)[0]

    def _is_avl(self, node):
        if node is None:
            return True, 0
        left_is_avl, left_height = self._is_avl(node.left)
        right_is_avl, right_height = self._is_avl(node.right)
        balanced = abs(left_height - right_height) <= 1
        is_avl = left_is_avl and right_is_avl and balanced
        height = max(left_height, right_height) + 1
        return is_avl, height
#18 It returns the maximum value of the results of calling itself recursively
# between the left and right subtrees of the binary tree x.
#19
    def is_heap(self):
        return self._is_heap(self.root)

    def _is_heap(self, node):
        if node is None:
            return True
        if node.left and len(node.left.key) > len(node.key):
            return False
        if node.right and len(node.right.key) > len(node.key):
            return False
        return self._is_heap(node.left) and self._is_heap(node.right)


# Example usage:
bst_str = Binarysearchtree()
bst_str.insert("Toyota")
bst_str.insert("Hyundai")
bst_str.insert("Mercedes")
bst_str.insert("Audi")
bst_str.insert("Porche")
bst_str.insert("LandRover")

print("Traverse a tree:", bst_str.breadth())
print()

print("Pre-order traverse:", end=" ")
bst_str.preorder(bst_str.root)
print()
print("In-order traverse:", end=" ")
bst_str.inorder(bst_str.root)
print()

print("Post-order traverse:", end=" ")
bst_str.postorder(bst_str.root)
print()

print("Number of node:", bst_str.count())
print("Min value:", bst_str.min())
print("Max value:", bst_str.max())
print("Sum of all values:", bst_str.sum())
print("Average length of all values:", bst_str.avg())

deleted_node = "Audi"
print(f"Delete node with value {deleted_node}")
bst_str.dele(deleted_node)
print()

print("In-order after deleting:", end=" ")
bst_str.inorder(bst_str.root)
print()

print("Height:", bst_str.height())
print("Cost of the most expensive path:", bst_str.cost_of_most_expensive_path())

print("Is AVL?:", bst_str.is_avl())
print("Is Heap?:", bst_str.is_heap())
