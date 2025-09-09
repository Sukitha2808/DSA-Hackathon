class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)
root = Node(100)
root.left = Node(150)
root.right = Node(200)
root.left.left = Node(250)
root.left.right = Node(500)
root.left.right.left = Node(550)
root.left.right.right = Node(600)
preorder(root)