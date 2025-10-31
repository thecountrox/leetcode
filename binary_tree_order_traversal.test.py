class Node:
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def binaryTreeLevelOrder(self, root: Node) -> list[list[str]]:
        res = []

        def backtrack(level: int, node: Node | None):
            # if root is None then stop
            if node is None:
                return

            # add a level if there is a new level
            if len(res) <= level:
                res.append([])

            # then add current and backtrack from there
            res[level].append(node.val)
            backtrack(level + 1, node.left)
            backtrack(level + 1, node.right)

        backtrack(0, root)
        return res


#      5
#     / \
#   12   13
#   /  \    \
#  7    14    2
# /  \  /  \  / \
# 17  23 27 3 8  11

root = Node(val=5)
root.left = Node(val=12)
root.right = Node(val=13)

root.left.left = Node(val=7)
root.left.right = Node(val=14)

root.right.right = Node(val=2)

root.left.left.left = Node(val=17)
root.left.left.right = Node(val=23)

root.left.right.left = Node(val=27)
root.left.right.right = Node(val=3)

root.right.right.left = Node(val=8)
root.right.right.right = Node(val=11)


s = Solution()
print(s.binaryTreeLevelOrder(root))
