from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def backtrack(root, level, res):
            if root is None:
                return
            if len(res) <= level:
                res.append([])

            res[level].append(root.val)

            backtrack(root.left, level + 1, res)
            backtrack(root.right, level + 1, res)

        backtrack(root, 0, res)
        return res
