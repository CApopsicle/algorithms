#958. Check Completeness of a Binary Tree
# Completeness: In a complete binary tree every level, 
# except possibly the last, is completely filled, 
# and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.

# Example1:
#       1
#     /   \
#    2     3
#   / \
#  4   5
# True

# Example2:
#       1
#     /   \
#    2     3
#   / \      \
#  4  5       7
# False

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Give every node a position number, left child = root*2, right child = root*2+1
# O(N) Time, where N is the number of nodes of the tree
# We have to bfs traverse the tree

def isCompleteTree(root):
    '''
    input: root: TreeNode
    output: bool
    '''
    nodes = [(root, 1)]
    i = 0
    while i < len(nodes):
        node, pos = nodes[i]
        if node.left:
            nodes.append((node.left, pos * 2))
        if node.right:
            nodes.append((node.right, pos * 2 + 1))
        i += 1
    return nodes[-1][1] == len(nodes)
