""" """

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(target: int, idx: int, currentCombination: list):
            if target == 0:
                res.append(currentCombination.copy())
                return

            for i in range(idx, n + 1):
                currentCombination.append(i)
                backtrack(target - 1, i + 1, currentCombination)
                currentCombination.pop()

        backtrack(target=k, idx=1, currentCombination=[])
        return res


s = Solution()
print(s.combine(4, 2))
