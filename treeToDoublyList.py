#426. Convert Binary Search Tree to Sorted Doubly Linked List

# Convert a BST to a sorted circular doubly-linked list in-place

# input
#      4 
#     /  \
#    2    5
#   / \
#  1   3

# output
# 1  <->  2 <-> 3 <-> 4 <-> 5
# \                         /
#  -------------------------

# Use DFS inorder traversal
# traverse(left)
# do something to current node
# traverse(right)

def treeToDoublyList(root):
    def helper(node):
        if node.left:
            helper(node.left)

        if last is not None:
            last.right = node
            node.left = last
        if first is None:
            first = node
        last = node
        
        if node.right:
            helper(node.right)

    #Keep track of first node `1` and last node `5`
    first, last = None, None
    helper(root)
    last.right = first
    first.left = last
    return first