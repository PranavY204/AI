class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def iddfs(root, goal):
    for d in range(100000):
        res = dls(root, goal, d)
        if res:
            return "Found"
    return "Not Found"

def dls(root, goal, depth):
    if depth == 0:
        if root.value == goal:
            return True
        return False
    for child in root.children:
        if dls(child, goal, depth - 1):
            return True
    return False

root = TreeNode('Y')
node2 = TreeNode('P')
node3 = TreeNode('X')
node4 = TreeNode('R')
node5 = TreeNode('S')
node6 = TreeNode('F')
node7 = TreeNode('H')

root.add_child(node2)
root.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)
node3.add_child(node6)
node3.add_child(node7)

print(iddfs(root, 'F'))
