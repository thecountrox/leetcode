"""
at first glance this problem looks exactly like combsum,
except u cannot repeat anything, which means i dont have to use a loop
the base case would be running out of numbers in nums.
it should be skip or take exclusively before moving on

2 base case would be
if idx > n then stop
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(idx: int, current_set: list[int]):
            if idx == n:
                res.append(current_set.copy())
                return
            # add current one
            current_set.append(nums[idx])
            backtrack(idx + 1, current_set)

            # or skip current one
            current_set.pop()
            backtrack(idx + 1, current_set)

        backtrack(0, [])

        return res


s = Solution()
print(s.subsets([1, 2, 3]))
