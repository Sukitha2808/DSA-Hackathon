class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def getHeight(root):
    if root is None:
        return 0 
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    return max(left_height, right_height) + 1

root = Tree(150)
root.left = Tree(200)
root.right = Tree(300)
root.left.left = Tree(400)
root.right.left = Tree(500)
root.right.right = Tree(600)
root.right.left.left = Tree(700)
root.right.right.left = Tree(800)
root.right.left.right = Tree(900)
root.right.right .right= Tree(1000)
print("Height of the tree :", getHeight(root))