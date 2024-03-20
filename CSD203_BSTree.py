class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Bird:
    def __init__(self, type="", rate="", wing=-1):
        self.Type = type
        self.Rate = rate
        self.Wing = wing
    def __repr__(self):
        return f"({self.Type}, {self.Rate}, {self.Wing})"
class NodeQ:
    def __init__(a,data):
        a.data = data
        a.next = None
class MyQueue:
    def __init__(a):
        a.head = None
        a.tail = None
    def isEmpty(a):
        return a.head ==None
    def EnQueue(a, data):
        node = NodeQ(data)
        if a.isEmpty():
            a.head = node
            a.tail = node
        else:
            a.tail.next = node
            a.tail = node
    #end def
    def DeQueue(a):
        if a.isEmpty():
            return None
        data = a.head.data
        a.head = a.head.next
        return data
#end class
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")


    def insert(self, xType, xRate, xWing):
        if xType[0] == 'B' or xRate > 10:
            return
        bird = Bird(xType, xRate, xWing)
        if self.root is None:
            self.root = Node(bird)
            return
        current = self.root
        while True:
            if xRate < current.data.Rate:
                if current.left is None:
                    current.left = Node(bird)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(bird)
                    break
                else:
                    current = current.right

    def f2(self):
        self.preOrder2(self.root)
        print("")

    def preOrder2(self, p):
        if p == None:
            return
        if p.data.Price <= 10 and p.data.Price >= 4:
            self.visit(p)
        self.preOrder2(p.left)
        self.preOrder2(p.right)

    def f3(self):
        self.breadth_first2()
    def breadth_first2(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if p % 2 != 0:
                self.visit(p)
            if p.left != None:
                my.EnQueue(p.left)
            if p.right != None:
                my.EnQueue(p.right)
        print("")
    def f4(self):
        self.postOrder2()
    def postOrder2(self,p):
        if p==None:
            return
        if p.data.Wing <= 4 or p.data.Rate >6:
            self.postOrder(p.left)
            self.postOrder(p.right)
            self.visit(p)


    def f5(self):
        self.inOrder2()
    def inOrder2(self, p):
        if p == None:
            return
        if p.data.Type.startswith('A') or p.data.Type.startswith('C'):
            self.inOrder(p.left)
            self.visit(p)
            self.inOrder(p.right)

    def f6(self):
        self.delete_father_of_third_inorder_node(self.root)
        self.inVisit()

    def delete_father_of_third_inorder_node(self, root):
        if root is None:
            return None
        inorder_nodes = []
        self.inorder_traversal(root, inorder_nodes)
        if len(inorder_nodes) < 3:
            return
        third_node = inorder_nodes[2]
        if third_node.left is None and third_node.right is None:
            # If the third node has no children, we delete its parent
            self.delete_parent(root, third_node)
        elif third_node.left is None or third_node.right is None:
            # If the third node has only one child, we merge it with its parent
            self.merge_with_parent(root, third_node)

    def inorder_traversal(self, root, result):
        if root is None:
            return
        self.inorder_traversal(root.left, result)
        result.append(root)
        self.inorder_traversal(root.right, result)

    def delete_parent(self, root, node):
        if root is None:
            return None
        if root.left == node or root.right == node:
            return None
        if root.left:
            if root.left.data == node:
                root.left = None
        if root.right:
            if root.right.data == node:
                root.right = None
        self.delete_parent(root.left, node)
        self.delete_parent(root.right, node)

    def merge_with_parent(self, root, node):
        if root is None:
            return None
        if root.left == node:
            if node.left:
                root.left = node.left
            else:
                root.left = node.right
        if root.right == node:
            if node.left:
                root.right = node.left
            else:
                root.right = node.right
        self.merge_with_parent(root.left, node)
        self.merge_with_parent(root.right, node)

    def f7(self):
        self.delete_sixth_postorder_node(self.root)
        self.postVisit()

    def delete_sixth_postorder_node(self, root):
        if root is None:
            return None
        postorder_nodes = []
        self.postorder_traversal(root, postorder_nodes)
        if len(postorder_nodes) < 6:
            return
        sixth_node = postorder_nodes[5]
        self.delete_node_by_copying(root, sixth_node)

    def postorder_traversal(self, root, result):
        if root is None:
            return
        self.postorder_traversal(root.left, result)
        self.postorder_traversal(root.right, result)
        result.append(root)

    def delete_node_by_copying(self, root, node):
        if root is None:
            return
        if root.left == node:
            if node.left:
                root.left = node.left
            else:
                root.left = node.right
        if root.right == node:
            if node.left:
                root.right = node.left
            else:
                root.right = node.right
        self.delete_node_by_copying(root.left, node)
        self.delete_node_by_copying(root.right, node)

    def f8(self):
        height = self.find_height_of_fourth_preorder_node(self.root)
        self.set_wing_equal_to_height(self.root, height)
        self.inVisit()

    def find_height_of_fourth_preorder_node(self, root):
        if root is None:
            return 0
        preorder_nodes = []
        self.preorder_traversal(root, preorder_nodes)
        if len(preorder_nodes) < 4:
            return 0
        fourth_node = preorder_nodes[3]
        return self.height(fourth_node)

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def set_wing_equal_to_height(self, root, height):
        if root is None:
            return
        root.data.Wing = height
        self.set_wing_equal_to_height(root.left, height)
        self.set_wing_equal_to_height(root.right, height)

    def f9(self):
        height = self.find_height_of_sixth_inorder_node(self.root)
        self.set_wing_equal_to_height(self.root, height)
        self.inVisit()

    def find_height_of_sixth_inorder_node(self, root):
        if root is None:
            return 0
        inorder_nodes = []
        self.inorder_traversal(root, inorder_nodes)
        if len(inorder_nodes) < 6:
            return 0
        sixth_node = inorder_nodes[5]
        return self.height(sixth_node)

    def f10(self):
        self.rotate_first_node_with_two_children_and_rate_less_than_five(self.root)
        self.postVisit()

    def rotate_first_node_with_two_children_and_rate_less_than_five(self, root):
        if root is None:
            return None
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            if current.left and current.right and current.data.Rate < 5:
                self.rotate_right(current)
                return
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def rotate_right(self, node):
        if node is None:
            return
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        node = pivot

    def f11(self):
        self.rotate_first_node_with_right_son_and_rate_greater_than_seven(self.root)
        self.inVisit()

    def rotate_first_node_with_right_son_and_rate_greater_than_seven(self, root):
        if root is None:
            return None
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            if current.right and current.data.Rate > 7:
                self.rotate_left(current)
                return
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def rotate_left(self, node):
        if node is None:
            return
        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        node = pivot

