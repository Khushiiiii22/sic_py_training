'''Problem Statement
Height of a Binary Tree

Given the root node of a binary tree, write a function to compute the height of the tree.
The height of a binary tree is the number of edges on the longest path from the root node to a leaf node.
For a tree with only the root node, the height is 0.'''

class TreeNode:
    def __init__(self , x):
        self.value = x
        self.left = None
        self.right = None

def height(root):
        if root is None:
            return -1
        else:
            left_height = height(root.left)
            right_height = height(root.right)
            return 1 +max(left_height , right_height)
        

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


print(height(root))  # Output: 2



