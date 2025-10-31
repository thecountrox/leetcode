"""
Nary tree means instead of two children per node, we can have N children per node
This means we cannot use .left or .right traversals instead we do this dynamically
The children are given in a list of Nodes
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int | None = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        res = [[]]

        def backtrack(level: int, node: Node | None):
            if node is None:
                return

            if level > len(res):
                res.append([])

        backtrack(0, root)
        return res
