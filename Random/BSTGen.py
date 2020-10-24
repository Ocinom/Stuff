class Node():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree():

    def __init__(self, val=0):
        self.root = Node(val)
        self.cache = []

    def mTree(self, node):
        if node == None:
            return
        self.cache.append(node.val)
        self.mTree(node.left)
        self.mTree(node.right)

    def printTree(self, root):
        self.mTree(root)
        print(self.cache)
        print("-" * 10)
        self.cache = []

    def insert(self, val, node: Node):
        if node.val == val:
            return
        if val < node.val:
            if not node.left:
                node.left = Node(val)
            else:
                self.insert(val, node.left)
        if val > node.val:
            if not node.right:
                node.right = Node(val)
            else:
                self.insert(val, node.right)

    def invert(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.right)
        self.invert(node.left)

a = Tree(4)
a.insert(2, a.root)
a.insert(7, a.root)
a.insert(1, a.root)
a.insert(3, a.root)
a.insert(6, a.root)
a.insert(9, a.root)
a.printTree(a.root)
a.invert(a.root)
print(a.root.left.val) #7
print(a.root.left.left.val) #9
print(a.root.left.right.val) #6
print(a.root.right.val) #2
print(a.root.right.left.val) #3
print(a.root.right.right.val) #1
