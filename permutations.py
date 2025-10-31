from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(currentPermutation: list):
            if len(currentPermutation) == len(nums):
                res.append(currentPermutation.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    currentPermutation.append(nums[i])

                    backtrack(currentPermutation)

                    currentPermutation.pop()
                    used[i] = False

        backtrack([])
        return res


s = Solution()
print(s.permute([1, 1, 2]))
