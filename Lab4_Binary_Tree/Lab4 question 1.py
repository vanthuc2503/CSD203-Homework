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

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key
#11
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
        return node.key + self._sum(node.left) + self._sum(node.right)
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
        return node.key + max(left_cost, right_cost)
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
        if node.left and node.left.key > node.key:
            return False
        if node.right and node.right.key > node.key:
            return False
        return self._is_heap(node.left) and self._is_heap(node.right)


# Example usage:
bstree = Binarysearchtree()
bstree.insert(2)
bstree.insert(5)
bstree.insert(7)
bstree.insert(8)
bstree.insert(6)
bstree.insert(90)
bstree.insert(40)
bstree.insert(30)

print("Traverse a tree:")
print(bstree.breadth())

print("Pre-order traverse:", end=" ")
bstree.preorder(bstree.root)
print()

print("In-order traverse:", end=" ")
bstree.inorder(bstree.root)
print()

print("Post-order traverse:", end=" ")
bstree.postorder(bstree.root)
print()

print("Number of nodes:", bstree.count())
print("Min value:", bstree.min())
print("Max value:", bstree.max())
print("Sum of all values:", bstree.sum())
print("Average of all values:", bstree.avg())

node_to_delete = 8
print(f"Delete node with value {node_to_delete}")
bstree.dele(node_to_delete)
print()

print("In-order after deleting:", end=" ")
bstree.inorder(bstree.root)
print()

print("Height:", bstree.height())
print("Cost of the most expensive path:", bstree.cost_of_most_expensive_path())

print("Is AVL?:", bstree.is_avl())
print("Is Heap?:", bstree.is_heap())
