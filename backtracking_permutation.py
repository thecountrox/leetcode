class Solution:
    def permuteUnique(self, nums: list):
        res = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(currentPermutation):
            if len(currentPermutation) == len(nums):
                res.append(currentPermutation.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    currentPermutation.append(nums[i])

                    backtrack(currentPermutation)

                    currentPermutation.pop()
                    used[i] = False

        backtrack([])
        return res


s = Solution()
print(s.permuteUnique([1, 2, 3]))
