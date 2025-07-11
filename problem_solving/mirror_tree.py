#Mirror Tree
''' When a tree is reflected across an imaginary straight vertical line right or left of the entire tree, the resultant tree is the mirror tree of the original tree. Your task is to write a program to check if two given trees are mirrors of each other.
Input:
The first line consists of the number of nodes N.
The next N-1 lines describe the first tree. Each line has two integers U and V and a letter 'R' or 'L', denoting that V is the left or the right child of U.
The next N-1 lines describe the second tree. Each line has two integers U and V and a letter 'R' or 'L', denoting that V is the left or the right child of U.'''

class TreeNode:
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None

def build_tree(N):
    if N == 0:
        return None
    
    nodes_map ={}
    is_child = set()

    for i in range(1, N + 1):
        nodes_map[i] = TreeNode(i)

    for _ in range(N - 1):
        u, v, side = input().split()
        u = int(u)
        v = int(v)

        if u not in nodes_map:
            nodes_map[u] = TreeNode(u)
        if v not in nodes_map:
            nodes_map[v] = TreeNode(v)

        if side == 'L':
            nodes_map[u].left = nodes_map[v]
        else: # side == 'R'
            nodes_map[u].right = nodes_map[v]
        
        is_child.add(v)
    
    root = None
    for i in range(1, N + 1):
        if i in nodes_map and i not in is_child:
            root = nodes_map[i]
            break
    
    if N == 1 and 1 in nodes_map:
        root = nodes_map[1]
    elif N > 1 and root is None:

        if N == 1 and nodes_map:
            root = list(nodes_map.values())[0]

    return root


def are_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.value == root2.value and
            are_mirror(root1.left, root2.right) and
            are_mirror(root1.right, root2.left))

if __name__ == "__main__":
    N = int(input())
    root1 = build_tree(N)
    root2 = build_tree(N)
    if are_mirror(root1, root2):
        print("yes")
    else:
        print("no")

