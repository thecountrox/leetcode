from typing import Optional, List, final

@final
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def stub_function(tree: List[str]):
    pass

def preorderTraversal( root: Optional[TreeNode]) -> List[int]:
    res = []


    def traverse(root):
        res.append(root.val)
        if root.left is not None:
            res.append(root.left)
        else:
            res.append(root.right)
    return res
