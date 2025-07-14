#Zig Zag Traversal
#Your task is to write a program to print the zigzag level-order traversal of a binary tree.
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val = val
        self. left = None
        self.right = None

def build_tree(N,edges):
    nodes = {}
    children = set()
    for u , v , c in edges:
        if u not in nodes:
            nodes[u] = TreeNode(u)
        if v not in nodes:
            nodes[v] = TreeNode(v)
        if c == 'L':
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]
            children.add(v)
    
    root = None
    for node in nodes:
        if node not in children:
            root = nodes[node]
            break
    return root

def zigzag_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level_nodes.reverse()
        result.extend(level_nodes)
        left_to_right = not left_to_right
    return result

if __name__ == "__main__":
    N = int(input())
    edges = []
    for _ in range(N-1):
        u, v, c = input().split()
        edges.append((int(u), int(v), c))
    root = build_tree(N, edges)
    ans = zigzag_traversal(root)
    print(' '.join(map(str, ans)))
        
