'''
level order traversal
[3 9 20 null null 15 7] -> tree
'''
from typing import Optional

class Node:
    def __init__(self, val: int):
        self.data = val
        self.right = None
        self.left = None

def levelOrderTraversal(l: list[int|str])-> Optional[Node]:

    if len(l) <= 0 or l[0] == -1:
        return None
    root = Node(l[0]) # type: ignore
    queue = [root]
    idx = 1

    while len(queue) != 0 and idx < len(l) and l[idx] != -1:
        cur = queue.pop(0)

        # left node
        if l[idx] != 'null':
            cur.left = Node(l[idx]) # type: ignore
            queue.append(cur.left) # type: ignore
        idx +=1

        # check again
        if idx < len(l) or l[idx] == -1:
            break

        # right node

        if l[idx] != 'null':
            cur.right = Node(l[idx]) # type: ignore
            queue.append(cur.right) # type: ignore
        idx +=1

    return root

def dfs(root: Node | None)-> None:
    if root is None:
        return
    print(root.data, end="") 
    while root:
        dfs(root.left) # type:ignore
        dfs(root.right) # type:ignore
    return 

dfs(levelOrderTraversal([3,9,20,'null','null',15,7]))  
