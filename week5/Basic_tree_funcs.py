class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = None
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = Node()
    def insertAtRoot(self, value):
        temp = self.root
        self.root.val = value
        if self.root > temp:
            self.root.right = temp
        else:
            self.root.left = temp
    def insertAtLeaf(self, value):
        if value > self.root.val:
            temp = self.root.right
        if value < self.root.val:
            temp = temp.left
        while value > temp.val:
            temp = temp.right








    def compare(self, oldNode, newNode):
        if oldNode.val > newNode.val:
            return 1
        elif newNode.val > oldNode.val:
            return 0
        else:
            return -1
